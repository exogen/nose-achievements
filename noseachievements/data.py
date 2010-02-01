from cPickle import dump, load


class AchievementData(dict):
    @classmethod
    def load(cls, stream):
        data = load(stream)
        return cls(data)

    def save(self, stream):
        data = dict(self)
        data.pop('achievements.new', None)
        dump(data, stream, protocol=2)

    def unlock(self, achievement, value=True):
        unlocked = self.setdefault('achievements.unlocked', {})
        unlocked[achievement.id] = value
        self.setdefault('achievements.new', []).append(achievement)

    def is_unlocked(self, achievement):
        if not isinstance(achievement, basestring):
            achievement = achievement.id
        return achievement in self.get('achievements.unlocked', {})

