# -*- coding: utf-8 -*-
from datetime import time
from noseachievements.achievements.base import Achievement


class NightShift(Achievement):
    title = "Night Shift"
    message = "Don't you think it's getting a bit late?"
    start_shift = time(0, 0)
    end_shift = time(5, 0)
    template = u"""
     .·:´   |   *
 * ·::·   – ¤ –      %(announcement)s
  :::::     |
  :::::.        .:   %(title)s
   :::::`:·..·:´:'   %(subtitle)s
    `·::::::::·´  *  %(message)s
        ˘˘˘˘
"""

    def finalize(self, data, result):
        if data['result.tests'] and data['result.success']:
            start, finish = data['time.start'], data['time.finish']
            if (self.start_shift <= start.time() and
                self.end_shift > finish.time()):
                data.unlock(self, (start, finish))

