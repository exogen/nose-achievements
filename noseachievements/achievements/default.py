# -*- coding: utf-8 -*-
from datetime import datetime, time

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

