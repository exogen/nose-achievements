from cPickle import dump, load


class AchievementData(dict):
    def save(self, stream):
        dump(self, stream)

    @classmethod
    def load(cls, stream):
        return load(stream)

    def unlock(self, achievement):
        if achievement.key not in self['achievements.unlocked']:
            self['achievements.unlocked'][achievement.key] = achievement
            self['achievements.new'].append(achievement)

