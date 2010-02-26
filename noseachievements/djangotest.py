import os
import sys
import unittest
from optparse import OptionParser

from nose.config import Config
from django.test.simple import DjangoTestRunner, DjangoTestSuiteRunner

from noseachievements.plugin import AchievementsPlugin
from noseachievements.result import TextTestResult


class DjangoTestRunner(DjangoTestRunner):
    result_class = TextTestResult

    def __init__(self, *args, **kwargs):
        super(DjangoTestRunner, self).__init__(*args, **kwargs)
        self.plugin = AchievementsPlugin()
        parser = OptionParser()
        self.plugin.options(parser, os.environ)
        options, args = parser.parse_args([])
        self.plugin.configure(options, Config())
        self.plugin.enabled = True

    def run(self, *args, **kwargs):
        self.plugin.begin()
        result = super(DjangoTestRunner, self).run(*args, **kwargs)
        self.plugin.setOutputStream(sys.stdout)
        self.plugin.finalize(result)
        return result

    def _makeResult(self):
        # Monkeypatch TextTestRunner to avoid copying & pasting code. :(
        old_makeResult = unittest.TextTestRunner._makeResult
        runner = self
        def makeResult(self):
            return runner.result_class(self.stream, self.descriptions,
                                       self.verbosity, plugin=self.plugin)
        unittest.TextTestRunner._makeResult = makeResult
        result = super(DjangoTestRunner, self)._makeResult()
        unittest.TextTestRunner._makeResult = old_makeResult
        return result

class DjangoTestSuiteRunner(DjangoTestSuiteRunner):
    runner_class = DjangoTestRunner

    def run_suite(self, suite, **kwargs):
        return self.runner_class(verbosity=self.verbosity,
                                 failfast=self.failfast).run(suite)

