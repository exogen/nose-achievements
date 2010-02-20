import unittest

from nose.plugins import Plugin
from noseachievements.achievements.base import Achievement
from noseachievements.plugin import AchievementsPlugin

from helpers import PASS, TestPlugin


class TestDisabledPlugin(TestPlugin):
    activate = ''

    def test_is_plugin(self):
        self.assert_(isinstance(self.plugin, Plugin))

    def test_name_is_achievements(self):
        self.assertEqual(self.plugin.name, 'achievements')

    def test_is_not_enabled_by_default(self):
        self.assert_(not self.plugin.enabled)

    def test_has_data_dict(self):
        self.assert_(isinstance(self.plugin.data, dict))

    def test_data_is_not_shared(self):
        plugin = AchievementsPlugin()
        self.assert_(plugin.data is not self.plugin.data)

class TestEnabledPlugin(TestPlugin):
    data = {}

    def test_is_enabled(self):
        self.assert_(self.plugin.enabled)

    def test_no_achievements_are_loaded(self):
        self.assertEqual(len(self.plugin.achievements), 0)

    def test_no_achievements_are_printed(self):
        self.assert_("Ran 1 test" in self.output and
                     "OK" in self.output)

