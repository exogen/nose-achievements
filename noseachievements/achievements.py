# -*- coding: utf-8 -*-
import sys


class Achievement(object):
    TEMPLATE = u"""
  /.–==–.\\
 ( |   *| )
  ):    :(  Achievement unlocked!
    `::´
     ||     %(title)s
   .–''–.   %(line2)s
   |____|   %(line3)s
"""

    title = None
    level = None

    def beforeTest(self, test):
        pass

    def format(self):
        return self.TEMPLATE % {'title': self.title,
                                'line2': '',
                                'line3': ''}

class AreYouMockingMe(Achievement):
    title = "Are you mocking me?"
    modules = ['mock', 'mocker', 'pmock', 'dingus', 'mox', 'ludibrio',
               'minimock', 'mocktest', 'mocky', 'plone.mocktestcase',
               'pymock']

    def beforeTest(self, test):
        for module in self.modules:
            if module in sys.modules:
                return True

