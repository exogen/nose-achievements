import unittest
from datetime import datetime, timedelta
from noseachievements.achievements import get_achievement
from util import TestAchievement


achievement = get_achievement('night-shift')

class TestNightShiftAchievement(TestAchievement):
    achievements = [achievement()]

    def test_is_locked_from_5am_to_midnight(self):
        for hour in range(5, 12):
            self.data['time.start'] = datetime(2010, 1, 1, hour)
            self.data['time.finish'] = self.data['time.start']
            yield self._test_is_locked
        self.data['time.start'] = datetime(2010, 1, 1) - timedelta(microseconds=1)
        self.data['time.finish'] = self.data['time.start']
        yield self._test_is_locked

    def test_is_unlocked_from_midnight_to_5am(self):
        for hour in range(0, 5):
            self.data['time.start'] = datetime(2010, 1, 1, hour)
            self.data['time.finish'] = self.data['time.start']
            yield self._test_is_unlocked
        self.data['time.start'] = datetime(2010, 1, 1, 5) - timedelta(microseconds=1)
        self.data['time.finish'] = self.data['time.start']
        yield self._test_is_unlocked

