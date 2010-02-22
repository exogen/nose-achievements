from noseachievements.achievements.base import Achievement


class AchievementManager(object):
    def __init__(self, achievements=()):
        self.achievements = {}
        self.add_achievements(achievements)

    def __iter__(self):
        return self.achievements.itervalues()

    def __contains__(self, achievement):
        if not isinstance(achievement, basestring):
            achievement = achievement.key
        return achievement in self.achievements
    
    def __len__(self):
        return len(self.achievements)
    
    def add_achievement(self, achievement):
        self.achievements[achievement.key] = achievement

    def add_achievements(self, achievements):
        for achievement in achievements:
            self.add_achievement(achievement)

    def load(self):
        pass

class BuiltinAchievementManager(AchievementManager):
    def load(self):
        AchievementManager.load(self)

class EntryPointAchievementManager(AchievementManager):
    entry_point = 'nose.achievements'

    def __init__(self, entry_point=None):
        AchievementManager.__init__(self)
        if entry_point is not None:
            self.entry_point = entry_point

    def load(self):
        AchievementManager.load(self)
        from pkg_resources import iter_entry_points
        for entry_point in iter_entry_points(self.entry_point):
            achievement = entry_point.load()
            if callable(achievement):
                achievement = achievement()
            self.add_achievement(achievement)

try:
    from pkg_resources import iter_entry_points
except ImportError:
    default_manager = BuiltinAchievementManager()
else:
    default_manager = EntryPointAchievementManager()

class FilteredAchievementManager(AchievementManager):
    def __init__(self, keys, manager=default_manager):
        AchievementManager.__init__(self)
        if isinstance(keys, basestring):
            keys = keys.split(',')
        self.keys = keys
        if callable(manager):
            manager = manager()
        self.manager = manager

