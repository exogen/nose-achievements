from noseachievements.compat import pickle


class AchievementData(dict):
    PICKLE_PROTOCOL = 2

    def save(self, stream):
        pickle.dump(self, stream, self.PICKLE_PROTOCOL)

    @classmethod
    def load(cls, stream):
        return pickle.load(stream)

    def unlock(self, achievement):
        if achievement.key not in self['achievements.unlocked']:
            self['achievements.unlocked'][achievement.key] = achievement
            self['achievements.new'].append(achievement)

