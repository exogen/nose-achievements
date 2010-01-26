import sys
import codecs
import logging

from nose.plugins.base import Plugin
from pkg_resources import iter_entry_points


log = logging.getLogger(__name__)


class Achievements(Plugin):
    achieved = {}
    score = 0

    def options(self, parser, env):
        Plugin.options(self, parser, env)

    def configure(self, options, conf):
        Plugin.configure(self, options, conf)

    def begin(self):
        self.achievements = []
        for entry_point in iter_entry_points('nose.achievements'):
            achievement = entry_point.load()
            achievement.__achievement__ = entry_point.name
            self.achievements.append(achievement())

    def beforeTest(self, test):
        for achievement in self.achievements:
            if achievement.beforeTest(test):
                self.achieved[achievement] = True

    def report(self, stream):
        self.report_stream = stream

    def finalize(self, result):
        stream = codecs.getwriter('utf8')(self.report_stream)
        for achievement, data in self.achieved.iteritems():
            banner = achievement.format()
            stream.write(u"\n%s\n" % banner)

