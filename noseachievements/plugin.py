import os
import sys
import codecs
import logging
from datetime import datetime
from nose.plugins.base import Plugin
from pkg_resources import iter_entry_points
from noseachievements.data import AchievementData


log = logging.getLogger(__name__)

class Achievements(Plugin):
    name = 'achievements'
    score = 0
    filename_default = '.achievements'
    filename_env = 'ACHIEVEMENTS_FILE'

    def __init__(self, achievements=None, data=None, save=True):
        Plugin.__init__(self)
        self.discovery = achievements is None
        self.achievements = list(achievements or [])
        self.data = data
        if save:
            filename = os.environ.get(self.filename_env, self.filename_default)
            self.filename = os.path.abspath(filename)
        else:
            self.filename = None

    def options(self, parser, env):
        Plugin.options(self, parser, env)

    def configure(self, options, conf):
        Plugin.configure(self, options, conf)

    def load_data(self):
        if self.data is None and self.filename is not None:
            log.debug("Reading achievement data from %s...", self.filename)
            try:
                data_file = open(self.filename, 'rb')
                return AchievementData.load(data_file)
            except (IOError, EOFError):
                pass
        log.debug("Starting with new achievement data.")
        if self.data is None:
            return AchievementData()
        else:
            return self.data

    def save_data(self):
        if self.filename is not None:
            log.debug("Writing achievement data to %s...", self.filename)
            data_file = open(self.filename, 'wb')
            self.data.save(data_file)

    def begin(self):
        self.data = self.load_data()
        if self.discovery:
            for entry_point in iter_entry_points('nose.achievements'):
                achievement = entry_point.load()
                achievement.id = entry_point.name
                self.achievements.append(achievement())
        for achievement in self.achievements:
             achievement.begin(self.data)

    def afterTest(self, test):
        for achievement in self.achievements:
            achievement.afterTest(self.data, test)

    def prepareTest(self, test):
        #self.data['time.start'] = datetime.now()
        for achievement in self.achievements:
            achievement.prepareTest(self.data, test)

    def startTest(self, test):
        for achievement in self.achievements:
            achievement.startTest(self.data, test)

    def stopTest(self, test):
        for achievement in self.achievements:
            achievement.stopTest(self.data, test)

    def setOutputStream(self, stream):
        self.stream = stream
        #self.data['time.finish'] = datetime.now()
        for achievement in self.achievements:
            achievement.setOutputStream(self.data, stream)

    def report(self, stream):
        for achievement in self.achievements:
            achievement.report(self.data, stream)

    def finalize(self, result):
        self.data['result.errors'] = result.errors
        self.data['result.failures'] = result.failures
        self.data['result.tests'] = result.testsRun
        self.data['result.success'] = result.wasSuccessful()
        for achievement in self.achievements:
            achievement.finalize(self.data, result)
        self.save_data()
        unlocked = self.data.get('achievements.new', [])
        if unlocked:
            stream = codecs.getwriter('utf8')(self.stream)
            for achievement in unlocked:
                stream.write(u"\n%s\n" % achievement.banner())

