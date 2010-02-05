import unittest
from nose.plugins import Plugin
from noseachievements.achievements.base import Achievement
from noseachievements.plugin import AchievementsPlugin
from helpers import PASS, TestPlugin


class TestAchievement(TestPlugin):
    def setUp(self):
        self.achievement = Achievement()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_loaded(self):
        assert self.achievement in self.plugin.achievements

    def test_no_achievements_are_printed(self):
        self.assertEqual(unicode(self.output),
            ".\n%s\nRan 1 test in 0.000s\n\nOK\n" % ('-' * 70))

