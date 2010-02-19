# -*- coding: utf-8 -*-
import sys
from datetime import datetime, time, timedelta

from noseachievements.achievements.base import Achievement


class NightShift(Achievement):
    title = "Night Shift"
    message = "Don't you think it's getting a bit late?"
    template = u"""
     .·:´   |   *
 * ·::·   – ¤ –      %(announcement)s
  :::::     |
  :::::.        .:   %(title)s
   :::::`:·..·:´:'   %(subtitle)s
    `·::::::::·´  *  %(message)s
        ˘˘˘˘"""

    shift_start = time(0, 0)
    shift_end = time(5, 0)

    def finalize(self, data, result):
        if (result.testsRun > 0 and result.wasSuccessful() and
            self.shift_start <= data['time.start'].time() < self.shift_end and
            self.shift_start <= data['time.finish'].time() < self.shift_end):
            data.unlock(self)

class Punctuality(Achievement):
    title = "Punctuality"

    punctual_start = time(8, 59)
    punctual_end = time(9, 1)

    def finalize(self, data, result):
        if (result.testsRun > 0 and result.wasSuccessful() and
            (self.punctual_start <= data['time.start'].time() <
             self.punctual_end or self.punctual_start <=
             data['time.finish'].time() < self.punctual_end)):
            data.unlock(self)

class InstantFeedback(Achievement):
    title = "Instant Feedback"

    def finalize(self, data, result):
        duration = data['time.finish'] - data['time.start']
        if result.testsRun >= 50 and duration < timedelta(seconds=1):
            data.unlock(self)

class CoffeeBreak(Achievement):
    title = "Coffee Break"
    template = u"""
          (
        (  )
      .·:)::·.
   _.|`·::::·´|  %(announcement)s
 /,¯`,        |
 :'_.|        |  %(title)s
  `¯˘:        |  %(subtitle)s
      `·.__.·´"""

    def finalize(self, data, result):
        duration = data['time.finish'] - data['time.start']
        if timedelta(minutes=5) <= duration < timedelta(minutes=15):
            data.unlock(self)

class TakeAWalk(Achievement):
    title = "Take a Walk"

    def finalize(self, data, result):
        duration = data['time.finish'] - data['time.start']
        if timedelta(minutes=15) <= duration < timedelta(minutes=60):
            data.unlock(self)

class FullOfDots(Achievement):
    title = "My God, It's Full of Dots"

    def finalize(self, data, result):
        passing = result.testsRun - len(result.failures) - len(result.errors)
        if passing >= 2001:
            data.unlock(self)

class MockingMe(Achievement):
    title = "Are You Mocking Me?"
    mocking_modules = ['mock', 'mocker', 'pmock', 'dingus', 'mox', 'ludibrio',
                       'minimock', 'mocktest', 'mocky', 'plone.mocktestcase',
                       'pymock']

    def finalize(self, data, result):
        for module in self.mocking_modules:
            if module in sys.modules:
                data.unlock(self)
                break

class GreatExpectations(Achievement):
    title = "Great Expectations"

    def finalize(self, data, result):
        if 'expecter' in sys.modules:
            data.unlock(self)

class ToUnderstandRecursion(Achievement):
    title = "To Understand Recursion..."

