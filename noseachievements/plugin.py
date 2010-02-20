import codecs
from datetime import datetime

from nose.plugins import Plugin

from noseachievements.data import AchievementData
from noseachievements.achievements import DEFAULT_ACHIEVEMENTS


class AchievementsPlugin(Plugin):
    name = 'achievements'
    filename_env = 'ACHIEVEMENTS_FILE'
    score = -1000

    def __init__(self, achievements=None, data=None,
                 save_file='.achievements'):
        Plugin.__init__(self)
        if data is None:
            data = AchievementData()
        elif not isinstance(data, AchievementData):
            data = AchievementData(data)
        self.achievements = achievements
        self.data = data
        self.save_file = save_file

    def options(self, parser, env):
        Plugin.options(self, parser, env)
    
    def configure(self, options, conf):
        Plugin.configure(self, options, conf)
        if self.achievements is None:
            self.achievements = list(DEFAULT_ACHIEVEMENTS)

        self.data.setdefault('time.start', datetime.now())
        self.data.setdefault('achievements.pending', [])
        self.data.setdefault('achievements.unlocked', {})
        self.data.setdefault('result.string', '')
        self.data.setdefault('result.errors.exc_info', [])
        self.data.setdefault('result.failures.exc_info', [])
        
        for achievement in self.achievements:
            achievement.configure(self.data, options, conf)

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

        if self.save_file is not None:
            if isinstance(self.save_file, basestring):
                save_file = open(self.save_file, 'w')
            else:
                save_file = self.save_file
            self.data.save(save_file)

        output_stream = codecs.getwriter('utf-8')(self.output_stream)
        for achievement in self.data['achievements.pending']:
            output_stream.write(achievement.announcement() + '\n')

