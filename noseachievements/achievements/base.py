# -*- coding: utf-8 -*-


class Achievement(object):
    template = u"""
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
        return self.template % {'announcement': "Achievement unlocked!",
                                'title': self.title,
                                'subtitle': self.subtitle or "",
                                'message': self.message or ""}

