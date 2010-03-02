import logging
from noseachievements.compat import pickle


log = logging.getLogger(__name__)

class AchievementData(dict):
    PICKLE_PROTOCOL = 2

    def save(self, stream):
        pickle.dump(self, stream, self.PICKLE_PROTOCOL)

    @classmethod
    def load(cls, stream):
        try:
            return pickle.load(stream)
        except EOFError:
            log.warning("Empty data file, returning empty data")
            return cls()

    def unlock(self, achievement):
        if achievement.key not in self['achievements.unlocked']:
            self['achievements.unlocked'][achievement.key] = achievement
            self['achievements.new'].append(achievement)

