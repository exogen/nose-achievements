from django.test.simple import DjangoTestRunner, DjangoTestSuiteRunner

from noseachievements.plugin import AchievementsPlugin
from noseachievements.result import AchievementsTestResult
from noseachievements.runner import AchievementsTestRunner


class AchievementsDjangoTestResult(AchievementsTestResult):
    def stopTest(self, test):
        super(AchievementsDjangoTestResult, self).stopTest(test)
        if ((self._runner.failfast and not self.wasSuccessful()) or 
            self._runner._keyboard_interrupt_intercepted):
            self.stop()

class AchievementsDjangoTestRunner(DjangoTestRunner, AchievementsTestRunner):
    _result_class = AchievementsDjangoTestResult

    def _makeResult(self):
        result = super(AchievementsDjangoTestRunner, self)._makeResult()
        result._runner = self
        return result

class AchievementsDjangoTestSuiteRunner(DjangoTestSuiteRunner):
    _runner_class = AchievementsDjangoTestRunner

    def run_suite(self, suite, **kwargs):
        return self._runner_class(verbosity=self.verbosity,
                                  failfast=self.failfast).run(suite)

