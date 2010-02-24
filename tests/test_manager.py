import unittest

from nose.plugins.skip import SkipTest

import noseachievements.achievements.builtin
from noseachievements.manager import (AchievementManager,
                                      BuiltinAchievementManager,
                                      EntryPointAchievementManager,
                                      FilterAchievementManager)
from helpers import AlwaysUnlockedAchievement


class TestManager(unittest.TestCase):
    def setUp(self):
        self.achievements = [AlwaysUnlockedAchievement()]
        self.manager = AchievementManager(self.achievements * 2)
        self.manager.load()

    def test_does_not_add_duplicate_achievements(self):
        self.assertEqual(len(self.manager), 1)

    def test_achievement_key_is_in_manager(self):
        self.assertTrue(AlwaysUnlockedAchievement.key in self.manager)

    def test_other_instance_of_same_achievement_is_in_manager(self):
        self.assertTrue(AlwaysUnlockedAchievement() in self.manager)

    def test_iterating_manager_returns_achievements(self):
        self.assertEqual(list(self.manager), self.achievements)

class TestBuiltinAchievementManager(unittest.TestCase):
    def setUp(self):
        self.manager = BuiltinAchievementManager()
        self.manager.load()

    def test_includes_all_builtin_achievements(self):
        for name in noseachievements.achievements.builtin.__all__:
            achievement = getattr(noseachievements.achievements.builtin, name)()
            self.assertTrue(achievement in self.manager)

class TestFilterAchievementManager(unittest.TestCase):
    def setUp(self):
        self.manager = FilterAchievementManager('builtin', BuiltinAchievementManager)
        self.manager.load()
        self.builtin_manager = BuiltinAchievementManager()
        self.builtin_manager.load()

    def test_builtin_filter_includes_all_builtin_achievements(self):
        self.assertEqual(set(self.manager.achievements),
                         set(self.builtin_manager.achievements))

class TestFilterAchievementManagerAll(unittest.TestCase):
    def setUp(self):
        self.manager = FilterAchievementManager('all', BuiltinAchievementManager)
        self.manager.load()
        self.builtin_manager = BuiltinAchievementManager()
        self.builtin_manager.load()

    def test_builtin_filter_includes_all_builtin_achievements(self):
        self.assertEqual(set(self.manager.achievements),
                         set(self.builtin_manager.achievements))

class TestFilterAchievementManagerEmpty(unittest.TestCase):
    def setUp(self):
        self.manager = FilterAchievementManager('', BuiltinAchievementManager)
        self.manager.load()

    def test_empty_filter_includes_no_achievements(self):
        self.assertEqual(len(self.manager), 0)

class TestFilterAchievementManagerExclude(unittest.TestCase):
    def setUp(self):
        self.manager = FilterAchievementManager('-builtin:night-shift,'
                                                  '-builtin:punctuality',
                                                  BuiltinAchievementManager)
        self.manager.load()
        self.builtin_manager = BuiltinAchievementManager()
        self.builtin_manager.load()

    def test_achievements_are_excluded(self):
        achievements = set(self.builtin_manager.achievements)
        achievements.discard('builtin:night-shift')
        achievements.discard('builtin:punctuality')
        self.assertEqual(set(self.manager.achievements), achievements)

class TestFilterAchievementManagerExcludeAll(unittest.TestCase):
    def setUp(self):
        self.manager = FilterAchievementManager('-builtin',
                                                  BuiltinAchievementManager)
        self.manager.load()

    def test_all_achievements_are_excluded(self):
        self.assertEqual(len(self.manager), 0)

