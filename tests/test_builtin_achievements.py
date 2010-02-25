# -*- coding: utf-8 -*-
import unittest
from datetime import datetime

from noseachievements.achievements.builtin import (CompleteFailure, EpicFail,
    MinorLetdown, MajorLetdown, HappyEnding, NightShift, Punctuality,
    SausageFingers, ToUnderstandRecursion, InstantFeedback, CoffeeBreak,
    TakeAWalk, TakeANap, TakeAVacation, MockingMe, FullOfDots,
    GreatExpectations)

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

class TestNightShiftAchievementLastPassed(TestNightShiftAchievement):
    tests = [PASS]
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 0, 0),
            'history': [{'result.success': True}]}

class TestNightShiftAchievementUnlocked(TestPlugin):
    achievements = [NightShift]
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 0, 0),
            'history': [{'result.success': False}]}

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
            'time.finish': datetime(2010, 1, 1, 9, 0, 0),
            'history': [{'result.success': False}]}

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

class TestInstantFeedbackAchievementNotEnoughTests(TestPlugin):
    achievements = [InstantFeedback]
    tests = [PASS] * 49
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 0, 0, 1)}

    def test_achievement_is_locked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestInstantFeedbackAchievementTooSlow(TestPlugin):
    achievements = [InstantFeedback]
    tests = [PASS] * 49
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 0, 1, 0)}

    def test_achievement_is_locked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestInstantFeedbackAchievementUnlocked(TestPlugin):
    achievements = [InstantFeedback]
    tests = [ERROR] * 20 + [FAIL] * 20 + [PASS] * 10
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 0, 0, 1)}

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Instant Feedback" in self.output)

class TestCoffeeBreakAchievement(TestPlugin):
    achievements = [CoffeeBreak]
    tests = [PASS]
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 4, 59)}

    def test_achievement_is_locked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestCoffeeBreakAchievementUnlocked(TestPlugin):
    achievements = [CoffeeBreak]
    tests = [ERROR]
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 5, 0)}

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Coffee Break" in self.output)

class TestTakeAWalkAchievementUnlocked(TestPlugin):
    achievements = [TakeAWalk]
    tests = [ERROR]
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 0, 15, 0)}

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Take a Walk" in self.output)

class TestTakeANapAchievementUnlocked(TestPlugin):
    achievements = [TakeANap]
    tests = [ERROR]
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 1, 1, 0, 0)}

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Take a Nap" in self.output)

class TestTakeAVacationAchievementUnlocked(TestPlugin):
    achievements = [TakeAVacation]
    tests = [ERROR]
    data = {'time.start': datetime(2010, 1, 1, 0, 0, 0),
            'time.finish': datetime(2010, 1, 4, 0, 0, 0)}

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Take a Vacation" in self.output)

class TestMinorLetdownAchievementUnlocked(TestPlugin):
    achievements = [MinorLetdown]
    tests = [PASS] * 9 + [FAIL]

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Minor Letdown" in self.output)

class TestMajorLetdownAchievementUnlocked(TestPlugin):
    achievements = [MajorLetdown]
    tests = [PASS] * 99 + [FAIL]

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Major Letdown" in self.output)

class TestHappyEndingAchievementUnlocked(TestPlugin):
    achievements = [HappyEnding]
    tests = [FAIL] * 9 + [PASS]

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Happy Ending" in self.output)

class TestMockingMeAchievement(TestPlugin):
    achievements = [MockingMe({'foo': None, 'bar': None})]

    def test_achievement_is_locked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestMockingMeAchievementUnlocked(TestPlugin):
    achievements = [MockingMe({'dingus': None})]

    def test_achievement_is_locked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Are You Mocking Me?" in self.output)

class TestFullOfDotsAchievement(TestPlugin):
    achievements = [FullOfDots]
    tests = [PASS] * 2000

    def test_achievement_is_locked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestFullOfDotsAchievementUnlocked(TestPlugin):
    achievements = [FullOfDots]
    tests = [FAIL] + [PASS] * 2001

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "My God, It's Full of Dots" in self.output)

class TestGreatExpectationsAchievement(TestPlugin):
    achievements = [GreatExpectations({'expect': None})]

    def test_achievement_is_locked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestGreatExpectationsAchievementUnlocked(TestPlugin):
    achievements = [GreatExpectations({'expecter': None})]

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Great Expectations" in self.output)

