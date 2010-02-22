import logging
import codecs
from datetime import datetime

from nose.plugins import Plugin

from noseachievements.data import AchievementData
from noseachievements.manager import AchievementManager, default_manager


log = logging.getLogger(__name__)


class AchievementsPlugin(Plugin):
    name = 'achievements'
    score = -1000
    default_filename = '.achievements'

    def __init__(self, achievements=default_manager, data=None):
        Plugin.__init__(self)
        if callable(achievements):
            achievements = achievements()
        self.achievements = achievements
        self.data = AchievementData(data or {})

    def options(self, parser, env):
        Plugin.options(self, parser, env)
        parser.add_option('--achievements-file', action='store',
            default=env.get('ACHIEVEMENTS_FILE', self.default_filename),
            metavar='FILE', dest='data_filename')
    
    def configure(self, options, conf):
        Plugin.configure(self, options, conf)

        self.data_filename = options.data_filename or None

        if isinstance(self.achievements, AchievementManager):
            self.achievements.load()
        for achievement in self.achievements:
            achievement.configure(options, conf)

    def begin(self):
        if self.data_filename:
            try:
                data_file = open(self.data_filename, 'rb')
            except IOError:
                pass
            else:
                data = AchievementData.load(data_file)
                history = data.pop('history', [])
                history.append(data)
                del history[-10:]
                self.data.setdefault('history', history)
                self.data.setdefault('achievements.unlocked',
                                     data.get('achievements.unlocked', {}))

        self.data.setdefault('time.start', datetime.now())
        self.data.setdefault('achievements.unlocked', {})
        self.data.setdefault('achievements.new', [])
        self.data.setdefault('result.string', '')
        self.data.setdefault('result.errors.exc_info', [])
        self.data.setdefault('result.failures.exc_info', [])

    def formatError(self, test, err):
        self.data['result.string'] += 'E'
        self.data['result.errors.exc_info'].append(err)

    def formatFailure(self, test, err):
        self.data['result.string'] += 'F'
        self.data['result.failures.exc_info'].append(err)

    def afterTest(self, test):
        if test.passed is None:
            self.data['result.string'] += '.'

    def setOutputStream(self, stream):
        self.output_stream = stream

    def finalize(self, result):
        self.data.setdefault('time.finish', datetime.now())
        
        for achievement in self.achievements:
            achievement.finalize(self.data, result)

        if self.data_filename:
            data_file = open(self.data_filename, 'w')
            self.data.save(data_file)

        output_stream = codecs.getwriter('utf-8')(self.output_stream)
        for achievement in self.data['achievements.new']:
            output_stream.write(achievement.announcement() + '\n')

