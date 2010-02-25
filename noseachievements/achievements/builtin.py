# -*- coding: utf-8 -*-
import sys
import re
import math
from datetime import datetime, time, timedelta
from cStringIO import StringIO

from noseachievements.achievements.base import Achievement

__all__ = ['NightShift', 'Punctuality', 'InstantFeedback', 'CoffeeBreak',
           'TakeAWalk', 'FullOfDots', 'MockingMe', 'GreatExpectations',
           'CompleteFailure', 'EpicFail', 'MinorLetdown', 'MajorLetdown',
           'HappyEnding', 'ToUnderstandRecursion', 'TakeANap',
           'TakeAVacation', 'SausageFingers', 'CodeCoverage']


class NightShift(Achievement):
    key = 'builtin:night-shift'
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
        if (data['result.tests'] and data['result.success'] and
            data['history'] and
            not data['history'][-1].get('result.success', True) and
            self.shift_start <= data['time.start'].time() < self.shift_end and
            self.shift_start <= data['time.finish'].time() < self.shift_end):
            data.unlock(self)

class Punctuality(Achievement):
    key = 'builtin:punctuality'
    title = "Punctuality"

    punctual_start = time(8, 59)
    punctual_end = time(9, 1)

    def finalize(self, data, result):
        if (data['result.tests'] and data['result.success'] and
            data['history'] and
            not data['history'][-1].get('result.success', True) and
            (self.punctual_start <= data['time.start'].time() <
             self.punctual_end or self.punctual_start <=
             data['time.finish'].time() < self.punctual_end)):
            data.unlock(self)

class InstantFeedback(Achievement):
    key = 'builtin:instant-feedback'
    title = "Instant Feedback"

    def finalize(self, data, result):
        duration = data['time.finish'] - data['time.start']
        if len(data['result.tests']) >= 50 and duration < timedelta(seconds=1):
            data.unlock(self)

class CoffeeBreak(Achievement):
    key = 'builtin:coffee-break'
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
    key = 'builtin:take-a-walk'
    title = "Take a Walk"

    def finalize(self, data, result):
        duration = data['time.finish'] - data['time.start']
        if timedelta(minutes=15) <= duration < timedelta(minutes=60):
            data.unlock(self)

class TakeANap(Achievement):
    key = 'builtin:take-a-nap'
    title = "Take a Nap"

    def finalize(self, data, result):
        duration = data['time.finish'] - data['time.start']
        if timedelta(hours=1) <= duration < timedelta(hours=5):
            data.unlock(self)

class TakeAVacation(Achievement):
    key = 'builtin:take-a-vacation'
    title = "Take a Vacation"

    def finalize(self, data, result):
        duration = data['time.finish'] - data['time.start']
        if duration >= timedelta(days=3):
            data.unlock(self)

class CompleteFailure(Achievement):
    key = 'builtin:complete-failure'
    title = "Complete Failure"

    def finalize(self, data, result):
        if (50 <= len(data['result.tests']) <= 999 and
            len(data['result.tests']) == len(data['result.failures'])):
            data.unlock(self)

class EpicFail(Achievement):
    key = 'builtin:epic-fail'
    title = "Epic Fail"

    def finalize(self, data, result):
        if (len(data['result.tests']) >= 1000 and
            len(data['result.tests']) == len(data['result.failures'])):
            data.unlock(self)

class MinorLetdown(Achievement):
    key = 'builtin:minor-letdown'
    title = "Minor Letdown"
    
    def finalize(self, data, result):
        if re.match(r'[.]{9,98}[FE]$', data['result.string']):
            data.unlock(self)

class MajorLetdown(Achievement):
    key = 'builtin:major-letdown'
    title = "Major Letdown"

    def finalize(self, data, result):
        if re.match(r'[.]{99,}[FE]$', data['result.string']):
            data.unlock(self)

class HappyEnding(Achievement):
    key = 'builtin:happy-ending'
    title = "Happy Ending"

    def finalize(self, data, result):
        if re.match(r'[EF]{9,}[.]$', data['result.string']):
            data.unlock(self)

class FullOfDots(Achievement):
    key = 'builtin:my-god-its-full-of-dots'
    title = "My God, It's Full of Dots"

    def finalize(self, data, result):
        if data['result.string'].count('.') >= 2001:
            data.unlock(self)

class MockingMe(Achievement):
    key = 'builtin:mocking-me'
    title = "Are You Mocking Me?"
    mocking_modules = ['mock', 'mocker', 'pmock', 'dingus', 'mox', 'ludibrio',
                       'minimock', 'mocktest', 'mocky', 'plone.mocktestcase',
                       'pymock', 'fudge']

    def __init__(self, imported_modules=sys.modules):
        self.imported_modules = imported_modules

    def finalize(self, data, result):
        for module in self.mocking_modules:
            if module in self.imported_modules:
                data.unlock(self)
                break

class GreatExpectations(Achievement):
    key = 'builtin:great-expectations'
    title = "Great Expectations"

    def __init__(self, imported_modules=sys.modules):
        self.imported_modules = imported_modules

    def finalize(self, data, result):
        if 'expecter' in self.imported_modules:
            data.unlock(self)

class ToUnderstandRecursion(Achievement):
    key = 'builtin:to-understand-recursion'
    title = "To Understand Recursion..."

    def finalize(self, data, result):
        for test, (type_, value, exc_string) in data['result.errors']:
            if exc_string.endswith("RuntimeError: maximum recursion depth "
                                   "exceeded\n"):
                data.unlock(self)
                break

class SausageFingers(Achievement):
    key = 'builtin:sausage-fingers'
    title = "Sausage Fingers"

    def finalize(self, data, result):
        syntax_errors = set()
        for test, (type_, value, exc_string) in data['result.errors']:
            if type_ is SyntaxError:
                syntax_errors.add((value.filename, value.lineno))
        if len(syntax_errors) > 1:
            data.unlock(self)

class CodeCoverage(Achievement):
    key = 'builtin:100-code-coverage'
    title = "100% Code Coverage"
    template = u"""
            .
         .cd'b;
     _  (xk',kx)
   ckko  lk kd/      %(announcement)s
  (kk.`l_)k k(_,dl,
   `·q. lk',kp'´dk)  %(title)s
    _)k.'q k',.d·´   %(subtitle)s
   ldxkkp, ,xq(_     %(message)s
    `-^·´u|u^-·´
          |"""

    def configure(self, options, conf):
        self.enabled = options.enable_plugin_coverage
        if self.enabled:
            try:
                from coverage import coverage
            except ImportError:
                self.enabled = False
            else:
                self.coverage = coverage

    def finalize(self, data, result):
        if self.enabled and data['result.success']:
            coverage = self.coverage()
            coverage.load()
            report = StringIO()
            coverage.report(file=report)
            report_string = report.getvalue()
            last_line = report_string.splitlines()[-1]
            match = re.match(r'TOTAL\s+(?P<stmts>\d+)\s+(?P<exec>\d+)\s+'
                             r'(?P<cover>\d+)%', last_line)
            if match:
                statements = int(match.group('stmts'))
                executed = int(match.group('exec'))
                percent_covered = int(match.group('cover'))
                if percent_covered == 100:
                    level = int(math.log(statements, 2) - 7)
                    data.unlock(self)

