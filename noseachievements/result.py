import unittest

from nose.util import test_address


class TextTestResult(unittest._TextTestResult):
    def __init__(self, *args, **kwargs):
        self.plugin = kwargs.pop('plugin', None)
        unittest._TextTestResult.__init__(self, *args, **kwargs)

    def addSuccess(self, test):
        self.plugin.addSuccess(test)
        self.plugin.afterTest(test)
        return unittest._TextTestResult.addSuccess(self, test)

    def addError(self, test, err):
        self.plugin.addError(test, err)
        self.plugin.afterTest(test)
        return unittest._TextTestResult.addError(self, test, err)

    def addFailure(self, test, err):
        self.plugin.addFailure(test, err)
        self.plugin.afterTest(test)
        return unittest._TextTestResult.addFailure(self, test, err)

