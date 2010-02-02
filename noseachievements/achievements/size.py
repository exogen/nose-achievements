from noseachievements.achivements.base import Achievement


class FullOfDots(Achievement):
    def finalize(self, data, result):
        passing_tests = data['result.tests']
        passing_tests -= len(data['result.failures'])
        passing_tests -= len(data['result.errors'])
        if passing_tests >= 2001:
            data.unlock(self, passing_tests)

