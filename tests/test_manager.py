import unittest

from noseachievements.manager import (AchievementManager,
                                      BuiltinAchievementManager,
                                      EntryPointAchievementManager,
                                      FilteredAchievementManager)

from helpers import AlwaysUnlockedAchievement


class TestManager(unittest.TestCase):
    def setUp(self):
        self.achievements = [AlwaysUnlockedAchievement()]
        self.manager = AchievementManager(self.achievements * 2)

    def test_does_not_add_duplicate_achievements(self):
        self.assertEqual(len(self.manager), 1)

    def test_achievement_key_is_in_manager(self):
        self.assertTrue(AlwaysUnlockedAchievement.key in self.manager)

    def test_achievement_is_in_manager(self):
        self.assertTrue(AlwaysUnlockedAchievement() in self.manager)

    def test_iterating_manager_returns_achievements(self):
        self.assertEqual(list(self.manager), self.achievements)

