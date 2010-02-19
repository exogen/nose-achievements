import unittest
from datetime import datetime

from noseachievements.achievements.default import NightShift, Punctuality

from helpers import TestPlugin, PASS, FAIL, ERROR


class TestNightShiftAchievement(TestPlugin):
    data = {'time.start': datetime(2010, 1, 1, 23, 59, 59),
            'time.finish': datetime(2010, 1, 1, 23, 59, 59)}

    def setUp(self):
        self.achievement = NightShift()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked" not in self.output and
                     "Night Shift" not in self.output)

class TestNightShiftAchievementFailures(TestNightShiftAchievement):
    tests = [PASS, FAIL]
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 0, 0)}

class TestNightShiftAchievementErrors(TestNightShiftAchievement):
    tests = [PASS, ERROR]
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 0, 0)}

class TestNightShiftAchievementUnlocked(TestPlugin):
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 0, 0)}

    def setUp(self):
        self.achievement = NightShift()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked" in self.output and
                     "Night Shift" in self.output)

class TestPunctualityAchievement(TestPlugin):
    data = {'time.start': datetime(2010, 1, 1, 8, 58, 59),
            'time.finish': datetime(2010, 1, 1, 8, 58, 59)}

    def setUp(self):
        self.achievement = Punctuality()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked" not in self.output and
                     "Punctuality" not in self.output)

class TestPunctualityAchievementFailures(TestPunctualityAchievement):
    tests = [PASS, FAIL]
    data = {'time.start': datetime(2010, 1, 1, 9, 0, 0),
            'time.finish': datetime(2010, 1, 1, 9, 0, 0)}

class TestPunctualityAchievementErrors(TestPunctualityAchievement):
    tests = [PASS, ERROR]
    data = {'time.start': datetime(2010, 1, 1, 9, 0, 0),
            'time.finish': datetime(2010, 1, 1, 9, 0, 0)}

class TestPunctualityAchievementUnlocked(TestPlugin):
    data = {'time.start': datetime(2010, 1, 1, 9, 0, 0),
            'time.finish': datetime(2010, 1, 1, 9, 0, 0)}

    def setUp(self):
        self.achievement = Punctuality()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked" in self.output and
                     "Punctuality" in self.output)

