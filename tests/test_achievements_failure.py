# -*- coding: utf-8 -*-
import unittest

from noseachievements.achievements.default import CompleteFailure, EpicFail, \
    MinorLetdown, MajorLetdown, HappyEnding

from helpers import PASS, FAIL, ERROR, TestPlugin


class TestCompleteFailureAchievement(TestPlugin):
    tests = [FAIL] * 49

    def setUp(self):
        self.achievement = CompleteFailure()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestCompleteFailureAchievementUnlocked(TestPlugin):
    tests = [FAIL] * 999

    def setUp(self):
        self.achievement = CompleteFailure()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Complete Failure" in self.output)

class TestEpicFailAchievement(TestPlugin):
    tests = [FAIL] * 999

    def setUp(self):
        self.achievement = EpicFail()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestEpicFailAchievementUnlocked(TestPlugin):
    tests = [FAIL] * 1000

    def setUp(self):
        self.achievement = EpicFail()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "Epic Fail" in self.output)

class TestMinorLetdownAchievement(TestPlugin):
    tests = [FAIL] + [PASS] * 9

    def setUp(self):
        self.achievement = MinorLetdown()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked!" not in self.output)

