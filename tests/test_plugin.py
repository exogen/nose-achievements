import unittest

from nose.plugins import Plugin

from noseachievements.achievements.base import Achievement
from noseachievements.manager import default_manager, FilterAchievementManager
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

class TestPluginWithAchievementFilterInclude(TestPlugin):
    achievements = default_manager
    args = TestPlugin.args + ['--achievements=builtin:night-shift']

    def test_manager_is_filter_achievement_manager(self):
        self.assertTrue(isinstance(self.plugin.achievements,
                                   FilterAchievementManager))

    def test_manager_includes_achievement(self):
        self.assertEqual(self.plugin.achievements.include_keys,
                         set(['builtin:night-shift']))

    def test_manager_excludes_none(self):
        self.assertEqual(self.plugin.achievements.exclude_keys, set())

class TestPluginWithAchievementFilterAll(TestPlugin):
    args = TestPlugin.args + ['--achievements=all']

    def test_manager_includes_all(self):
        self.assertEqual(self.plugin.achievements.include_keys, set(['all']))

    def test_manager_excludes_none(self):
        self.assertEqual(self.plugin.achievements.exclude_keys, set())

class TestPluginWithAchievementFilterExclude(TestPlugin):
    args = TestPlugin.args + ['--achievements='
                              '-builtin:night-shift,-builtin:coffee-break']
    
    def test_manager_excludes_achievements(self):
        self.assertEqual(self.plugin.achievements.exclude_keys,
                         set(['builtin:night-shift', 'builtin:coffee-break']))

    def test_manager_includes_all(self):
        self.assertEqual(self.plugin.achievements.include_keys, set(['all']))

class TestPluginWithAchievementFilterEmpty(TestPlugin):
    args = TestPlugin.args + ['--achievements=']

    def test_manager_includes_empty_string(self):
        self.assertEqual(self.plugin.achievements.include_keys, set(['']))
    
    def test_manager_exculdes_none(self):
        self.assertEqual(self.plugin.achievements.exclude_keys, set())
