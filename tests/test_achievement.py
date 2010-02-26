# -*- coding: utf-8 -*-
import unittest

from noseachievements.achievements.base import Achievement
from noseachievements.compat import unicode

from helpers import (PASS, TestPlugin, NeverUnlockedAchievement,
    AlwaysUnlockedAchievement)


class TestAchievement(TestPlugin):
    achievement = NeverUnlockedAchievement()
    achievements = [achievement]

    def test_achievement_is_loaded(self):
        self.assert_(self.achievement in self.plugin.achievements)

    def test_no_achievements_are_printed(self):
        self.assert_("Ran 1 test" in self.output)
        self.assert_("Achievement unlocked" not in self.output)

    def test_announcement_returns_unlocked_string(self):
        self.assertEqual(self.achievement.announcement(), unicode("""
  /.–==*==–.\\
 ( |      #| ) Achievement unlocked!
  ):      ':(
    `·…_…·´    Test Achievement
      `H´      Test Subtitle
     _.U._     Test Message
    [_____]""", 'utf-8'))


class TestUnlockedAchievement(TestPlugin):
    def setUp(self):
        self.achievement = AlwaysUnlockedAchievement()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_printed(self):
        self.assert_("""
  /.–==*==–.\\
 ( |      #| ) Achievement unlocked!
  ):      ':(
    `·…_…·´    Test Achievement
      `H´      Test Subtitle
     _.U._     Test Message
    [_____]""" in self.output)
            

