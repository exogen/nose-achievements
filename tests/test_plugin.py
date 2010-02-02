import unittest
from nose.plugins import Plugin
from noseachievements.plugin import Achievements
from nose.plugins.plugintest import PluginTester
from helpers import PASS


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.plugin = Achievements()

    def test_is_plugin(self):
        assert isinstance(self.plugin, Plugin)

    def test_name_is_achievements(self):
        assert self.plugin.name == 'achievements'

    def test_is_not_enabled_by_default(self):
        assert self.plugin.enabled == False

class TestActivatedPlugin(PluginTester):
    activate = '--with-achievements'
    plugin = Achievements()
    plugins = [plugin]

    def makeSuite(self):
        return unittest.TestSuite([PASS])

    def test_is_enabled(self):
        assert self.plugin.enabled

    def test_has_data_dict(self):
        assert isinstance(self.plugin.data, dict)

    def test_data_is_not_shared(self):
        plugin = Achievements()
        assert plugin.data is not self.plugin.data

