# -*- coding: utf-8 -*-
import unittest

from noseachievements.achievements.base import Achievement

from helpers import PASS, TestPlugin, AlwaysUnlockedAchievement


class TestAchievement(TestPlugin):
    def setUp(self):
        self.achievement = Achievement()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_loaded(self):
        self.assert_(self.achievement in self.plugin.achievements)

    def test_no_achievements_are_printed(self):
        self.assert_("Ran 1 test" in self.output)
        self.assert_("Achievement unlocked" not in self.output)

    def test_announcement_returns_unlocked_string(self):
        self.assertEqual(self.achievement.announcement(), u"""
  /.–==*==–.\\
 ( |      #| ) Achievement unlocked!
  ):      ':(
    `·…_…·´    
      `H´      
     _.U._     
    [_____]""")


class TestUnlockedAchievement(TestPlugin):
    def setUp(self):
        self.achievement = AlwaysUnlockedAchievement()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_printed(self):
        self.assert_(u"""
  /.–==*==–.\\
 ( |      #| ) Achievement unlocked!
  ):      ':(
    `·…_…·´    Test Achievement
      `H´      Test Subtitle
     _.U._     Test Message
    [_____]""".encode('utf-8') in self.output)
            

