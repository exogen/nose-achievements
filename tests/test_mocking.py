import unittest
from noseachievements.achievements import get_achievement
from util import TestAchievement, FAIL_SUITE

MOCKING_MODULES = ['mock', 'mocker', 'pmock', 'dingus', 'mox', 'ludibrio',
                   'minimock', 'mocktest', 'mocky', 'plone.mocktestcase',
                   'pymock']

achievement = get_achievement('are-you-mocking-me')

class TestMockingAchievement(TestAchievement):
    modules = {}
    achievements = [achievement(modules)]

    def tearDown(self):
        self.modules.clear()
        TestAchievement.tearDown(self)

    def test_mocking_modules_unlock_achievement(self):
        for module in MOCKING_MODULES:
            self.modules[module] = True
            yield self._test_is_unlocked

    def test_is_locked_with_other_modules(self):
        yield self._test_is_locked
        for module in ['foo', 'unittest', 'mock.fakemodule']:
            self.modules[module] = True
            yield self._test_is_locked

class TestMockingAchievementEmpty(TestAchievement):
    suite = []
    modules = {}
    achievements = [achievement(modules)]

    def tearDown(self):
        self.modules.clear()
        TestAchievement.tearDown(self)

    def test_is_locked_with_mocking_modules(self):
        for module in MOCKING_MODULES:
            self.modules[module] = True
            yield self._test_is_locked

    def test_is_locked_with_other_modules(self):
        yield self._test_is_locked
        for module in ['foo', 'unittest', 'mock.fakemodule']:
            self.modules[module] = True
            yield self._test_is_locked

class TestMockingAchievementFailing(TestMockingAchievementEmpty):
    suite = FAIL_SUITE
    modules = {}
    achievements = [achievement(modules)]

