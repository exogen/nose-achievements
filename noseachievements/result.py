import unittest


class AchievementsTestResult(unittest._TextTestResult):
    def __init__(self, *args, **kwargs):
        self.plugin = kwargs.pop('plugin', None)
        super(AchievementsTestResult, self).__init__(*args, **kwargs)

    def stopTest(self, test):
        self.plugin.afterTest(test)
        return super(AchievementsTestResult, self).stopTest(test)

    def addSuccess(self, test):
        self.plugin.addSuccess(test)
        return super(AchievementsTestResult, self).addSuccess(test)

    def addError(self, test, err):
        self.plugin.addError(test, err)
        return super(AchievementsTestResult, self).addError(test, err)

    def addFailure(self, test, err):
        self.plugin.addFailure(test, err)
        return super(AchievementsTestResult, self).addFailure(test, err)

