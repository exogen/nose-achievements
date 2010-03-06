import logging
import codecs
from traceback import format_exception
from datetime import datetime

from noseachievements.data import AchievementData
from noseachievements.manager import (AchievementManager,
    FilterAchievementManager, default_manager)

try:
    from nose.plugins import Plugin
except ImportError:
    Plugin = object
try:
    from nose.util import test_address
except ImportError:
    def test_address(test):
        return test.id()

# Python 3 compatibility:
from noseachievements.compat import callable, unicode


log = logging.getLogger(__name__)

class AchievementsPlugin(Plugin):
    name = 'achievements'
    score = -1000
    default_filename = '.achievements'
    default_achievements = 'all'

    def __init__(self, achievements=default_manager, data=None):
        super(AchievementsPlugin, self).__init__()
        if callable(achievements):
            achievements = achievements()
        if not isinstance(achievements, AchievementManager):
            achievements = AchievementManager(achievements)
        self.achievements = achievements
        self.data = AchievementData(data or {})
        self.output_stream = None

    def options(self, parser, env):
        if Plugin is not object:
            super(AchievementsPlugin, self).options(parser, env)

        parser.add_option('--achievements-file', action='store',
            default=env.get('ACHIEVEMENTS_FILE', self.default_filename),
            metavar='FILE', dest='data_filename',
            help="Load and save achievement data in FILE. "
                 "An empty string will disable loading and saving. "
                 "[ACHIEVEMENTS_FILE]")
        parser.add_option('--achievements', action='store',
            default=env.get('ACHIEVEMENTS', self.default_achievements),
            metavar='FILTER', dest='achievements',
            help="Select or exclude specific achievements or achievement "
                 "groups. [ACHIEVEMENTS]")
    
    def configure(self, options, conf):
        # Save a reference to the `Config` to access its `stream` in case
        # setOutputStream isn't called.
        self.config = conf
        if Plugin is not object:
            super(AchievementsPlugin, self).configure(options, conf)

        self.data_filename = options.data_filename or None

        if options.achievements is not None:
            self.achievements = FilterAchievementManager(options.achievements,
                                                         self.achievements)

        self.achievements.load()
        for achievement in self.achievements:
            achievement.configure(options, conf)

    def begin(self):
        history = []
        unlocked = {}
        if self.data_filename:
            try:
                data_file = open(self.data_filename, 'rb')
            except IOError:
                log.debug("Failed to read achievement data from %s",
                          self.data_filename)
            else:
                data = AchievementData.load(data_file)
                data_file.close()
                log.info("Loaded achievement data from %s",
                         self.data_filename)
                history = data.pop('history', history)
                history.append(data)
                del history[:-10]
                unlocked = data.get('achievements.unlocked', unlocked)

        self.data.setdefault('history', history)
        self.data.setdefault('achievements.unlocked', unlocked)
        self.data.setdefault('achievements.new', [])
        self.data.setdefault('result.tests', [])
        self.data.setdefault('result.string', '')
        self.data.setdefault('result.errors', [])
        self.data.setdefault('result.failures', [])
        self.data.setdefault('time.start', datetime.now())

    def addError(self, test, err):
        type_, value, traceback = err
        exc_string = "".join(format_exception(type_, value, traceback))
        self.data['result.string'] += 'E'
        self.data['result.errors'].append((test_address(test),
                                           (type_, value, exc_string)))

    def addFailure(self, test, err):
        type_, value, traceback = err
        exc_string = "".join(format_exception(type_, value, traceback))
        self.data['result.string'] += 'F'
        self.data['result.failures'].append((test_address(test),
                                             (type_, value, exc_string)))

    def addSuccess(self, test):
        self.data['result.string'] += '.'

    def afterTest(self, test):
        self.data['result.tests'].append(test_address(test))

    def setOutputStream(self, stream):
        self.output_stream = stream

    def finalize(self, result):
        self.data.setdefault('time.finish', datetime.now())
        self.data.setdefault('result.success', result.wasSuccessful())
        
        for achievement in self.achievements:
            if achievement.key not in self.data['achievements.unlocked']:
                achievement.finalize(self.data, result)

        if self.data_filename:
            try:
                data_file = open(self.data_filename, 'wb')
            except IOError:
                log.error("Failed to write achievement data to %s (I/O error)",
                          self.data_filename)
            else:
                log.info("Saving achievement data to %s", self.data_filename)
                self.data.save(data_file)
                data_file.close()

        output_stream = self.output_stream or self.config.stream
        if str is not unicode:
            output_stream = codecs.getwriter('utf-8')(output_stream)
        for achievement in self.data['achievements.new']:
            announcement = achievement.announcement()
            output_stream.write(announcement)
            output_stream.write('\n')

