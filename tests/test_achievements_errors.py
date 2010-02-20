import unittest

from noseachievements.achievements.default import ToUnderstandRecursion, \
    SausageFingers

from helpers import TestPlugin, PASS, FAIL, ERROR


def recursion_error_func():
    raise RuntimeError("maximum recursion depth exceeded")

def runtime_error_func():
    raise RuntimeError("blah")

class TestRecursionAchievement(TestPlugin):
    tests = [unittest.FunctionTestCase(runtime_error_func)]

    def setUp(self):
        self.achievement = ToUnderstandRecursion()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked!" not in self.output)

class TestRecursionAchievementUnlocked(TestPlugin):
    tests = [unittest.FunctionTestCase(recursion_error_func)]

    def setUp(self):
        self.achievement = ToUnderstandRecursion()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_unlocked(self):
        self.assert_("Achievement unlocked!" in self.output and
                     "To Understand Recursion..." in self.output)

class TestSausageFingersAchievement(TestPlugin):
    tests = [ERROR]

    def setUp(self):
        self.achievement = SausageFingers()
        self.achievements = [self.achievement]
        TestPlugin.setUp(self)

    def test_achievement_is_not_unlocked(self):
        self.assert_("Achievement unlocked!" not in self.output)

# class TestSausageFingersAchievementUnlocked(TestPlugin):
#     tests = [unittest.FunctionTestCase(
#         lambda: compile("def /", 'a.py', 'exec')),
#              unittest.FunctionTestCase(
#         lambda: compile("def /", 'b.py', 'exec'))]
# 
#     def setUp(self):
#         self.achievement = SausageFingers()
#         self.achievements = [self.achievement]
#         TestPlugin.setUp(self)
# 
#     def test_achievement_is_unlocked(self):
#         self.assert_("Achievement unlocked!" in self.output and
#                      "Sausage Fingers" in self.output)
# 
