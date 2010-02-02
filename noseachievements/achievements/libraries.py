import sys
from noseachievements.achievements.base import Achievement


class MockingMe(Achievement):
    title = "Are You Mocking Me?"
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

