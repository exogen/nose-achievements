from cPickle import dump, load


class AchievementData(dict):
    def save(self, stream):
        copy = AchievementData(self)
        copy.pop('achievements.pending', None)
        copy.pop('result.errors.exc_info', None)
        copy.pop('result.failures.exc_info', None)
        dump(copy, stream)

    @classmethod
    def load(cls, stream):
        return load(stream)

    def unlock(self, achievement):
        self['achievements.pending'].append(achievement)

