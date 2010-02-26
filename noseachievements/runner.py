import os
import sys
from unittest import TextTestRunner
from optparse import OptionParser

from noseachievements.result import AchievementsTestResult
from noseachievements.plugin import AchievementsPlugin

try:
    from nose.config import Config
except ImportError:
    config = None
else:
    config = Config()


class AchievementsTestRunner(TextTestRunner):
    _result_class = AchievementsTestResult

    def __init__(self, *args, **kwargs):
        plugin = kwargs.pop('plugin', None)
        super(AchievementsTestRunner, self).__init__(*args, **kwargs)
        if plugin is None:
            plugin = AchievementsPlugin()
        parser = OptionParser()
        plugin.options(parser, os.environ)
        options, args = parser.parse_args([])
        plugin.configure(options, config)
        plugin.enabled = True
        self.plugin = plugin

    def _makeResult(self):
        return self._result_class(self.stream, self.descriptions,
                                  self.verbosity, plugin=self.plugin)

    def run(self, test):
        self.plugin.begin()
        result = super(AchievementsTestRunner, self).run(test)
        self.plugin.setOutputStream(self.stream)
        self.plugin.finalize(result)
        return result

