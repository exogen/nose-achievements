# -*- coding: utf-8 -*-
import sys
from datetime import datetime, time


class Achievement(object):
    TEMPLATE = u"""
  /.–==*==–.\\
 ( |      #| ) %(announcement)s
  ):      ':(
    `·…_…·´    %(title)s
      `H´      %(subtitle)s
     _.U._     %(message)s
    |[___]|
"""

    title = None
    subtitle = None
    message = None

    def begin(self, data):
        pass

    def afterTest(self, data, test):
        pass

    def beforeTest(self, data, test):
        pass
    
    def finalize(self, data, result):
        pass

    def prepareTest(self, data, test):
        pass

    def report(self, data, stream):
        pass

    def setOutputStream(self, data, stream):
        pass

    def startTest(self, data, test):
        pass

    def stopTest(self, data, test):
        pass

    def banner(self):
        return self.TEMPLATE % {'announcement': "Achievement unlocked!",
                                'title': self.title,
                                'subtitle': self.subtitle or "",
                                'message': self.message or ""}

class MockingMe(Achievement):
    title = "Are You Mocking Me?"
    id = 'mocking-me'
    mocking_modules = ['mock', 'mocker', 'pmock', 'dingus', 'mox', 'ludibrio',
                       'minimock', 'mocktest', 'mocky', 'plone.mocktestcase',
                       'pymock']

    def __init__(self, imported_modules=sys.modules):
        Achievement.__init__(self)
        self.imported_modules = imported_modules

    def finalize(self, data, result):
        if result.testsRun and result.wasSuccessful():
            imported_mocking_modules = set()
            for module in self.mocking_modules:
                if module in self.imported_modules:
                    imported_mocking_modules.add(module)
            if imported_mocking_modules:
                data.unlock(self, imported_mocking_modules)

class NightShift(Achievement):
    title = "Night Shift"
    id = 'night-shift'
    start_shift = time(0, 0)
    end_shift = time(5, 0)

    def finalize(self, data, result):
        print data
        if data['result.tests'] and data['result.success']:
            start, finish = data['time.start'], data['time.finish']
            if (self.start_shift <= start.time() and
                self.end_shift > finish.time()):
                data.unlock(self, (start, finish))

