import unittest
from nose.plugins.plugintest import PluginTester
from noseachievements.plugin import AchievementsPlugin


def pass_func():
    assert True

def fail_func():
    assert False

def error_func():
    raise Exception

PASS = unittest.FunctionTestCase(pass_func)
FAIL = unittest.FunctionTestCase(fail_func)
ERROR = unittest.FunctionTestCase(error_func)

class TestPlugin(PluginTester, unittest.TestCase):
    activate = '--with-achievements'
    tests = [PASS]
    achievements = []

    def setUp(self):
        self.plugin = AchievementsPlugin(self.achievements)
        self.plugins = [self.plugin]
        PluginTester.setUp(self)

    def makeSuite(self):
        return unittest.TestSuite(self.tests)

