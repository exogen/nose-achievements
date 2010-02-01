import unittest
from noseachievements.plugin import Achievements
from noseachievements.data import AchievementData
from nose.plugins.plugintest import PluginTester


def pass_test():
    assert True

def fail_test():
    assert False

def error_test():
    raise Exception

EMPTY_SUITE = []
ERROR_SUITE = [unittest.FunctionTestCase(error_test)]
FAIL_SUITE = [unittest.FunctionTestCase(fail_test)]
PASS_SUITE = [unittest.FunctionTestCase(pass_test)]

class TestAchievement(PluginTester):
    activate = '--with-achievements'
    achievements = []
    suite = PASS_SUITE

    def __init__(self):
        PluginTester.__init__(self)
        self.data = AchievementData({'testing': 123})

    def setUp(self):
        self.plugins = [Achievements(self.achievements, self.data, save=False)]
        PluginTester.setUp(self)

    def tearDown(self):
        self.data.clear()

    def makeSuite(self):
        return unittest.TestSuite(self.suite)

    def _test_is_locked(self):
        assert "Achievement unlocked!" not in self.output
        assert self.achievements[0].title not in self.output

    def _test_is_unlocked(self):
        assert "Achievement unlocked!" in self.output
        assert self.achievements[0].title in self.output

