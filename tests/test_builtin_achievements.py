# -*- coding: utf-8 -*-
import unittest
from datetime import datetime

from noseachievements.achievements.builtin import (CompleteFailure, EpicFail,
    MinorLetdown, MajorLetdown, HappyEnding, NightShift, Punctuality,
    SausageFingers, ToUnderstandRecursion)

from helpers import PASS, FAIL, ERROR, TestPlugin, error_test

class TestNightShiftAchievement(TestPlugin):
    achievements = [NightShift]
    data = {'time.start': datetime(2010, 1, 1, 23, 59, 59),
            'time.finish': datetime(2010, 1, 1, 23, 59, 59)}

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
    achievements = [NightShift]
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 0, 0)}

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked" in self.output and
                     "Night Shift" in self.output)

class TestPunctualityAchievement(TestPlugin):
    achievements = [Punctuality]
    data = {'time.start': datetime(2010, 1, 1, 8, 58, 59),
            'time.finish': datetime(2010, 1, 1, 8, 58, 59)}

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
    achievements = [Punctuality]
    data = {'time.start': datetime(2010, 1, 1, 9, 0, 0),
            'time.finish': datetime(2010, 1, 1, 9, 0, 0)}

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked" in self.output and
                     "Punctuality" in self.output)

class TestCompleteFailureAchievement(TestPlugin):
    achievements = [CompleteFailure]
    tests = [FAIL] * 49

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestCompleteFailureAchievementUnlocked(TestPlugin):
    achievements = [CompleteFailure]
    tests = [FAIL] * 999

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Complete Failure" in self.output)

class TestEpicFailAchievement(TestPlugin):
    achievements = [EpicFail]
    tests = [FAIL] * 999

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestEpicFailAchievementUnlocked(TestPlugin):
    achievements = [EpicFail]
    tests = [FAIL] * 1000

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Epic Fail" in self.output)

class TestMinorLetdownAchievement(TestPlugin):
    achievements = [MinorLetdown]
    tests = [FAIL] + [PASS] * 9

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestRecursionAchievement(TestPlugin):
    achievements = [ToUnderstandRecursion]
    tests = [error_test(RuntimeError("foo"))]

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestRecursionAchievementUnlocked(TestPlugin):
    achievements = [ToUnderstandRecursion]
    tests = [error_test(RuntimeError("maximum recursion depth exceeded"))]

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "To Understand Recursion..." in self.output)

class TestSausageFingersAchievement(TestPlugin):
    achievements = [SausageFingers]
    tests = [ERROR]

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestSausageFingersAchievementUnlocked(TestPlugin):
    achievements = [SausageFingers]
    tests = [unittest.FunctionTestCase(
        lambda: compile("def /", 'a.py', 'exec')),
             unittest.FunctionTestCase(
        lambda: compile("def /", 'b.py', 'exec'))]

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Sausage Fingers" in self.output)

