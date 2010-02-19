from cPickle import dump, load


class AchievementData(dict):
    def save(self, stream):
        dump(self, stream)

    @classmethod
    def load(cls, stream):
        return load(stream)

    def unlock(self, achievement):
        self['achievements.pending'].append(achievement)

