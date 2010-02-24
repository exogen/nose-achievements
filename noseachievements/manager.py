import noseachievements.achievements.builtin
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
        if callable(achievement):
            achievement = achievement()
        self.achievements[achievement.key] = achievement

    def add_achievements(self, achievements):
        for achievement in achievements:
            self.add_achievement(achievement)

    def load(self):
        pass

class BuiltinAchievementManager(AchievementManager):
    def load(self):
        AchievementManager.load(self)
        for name in noseachievements.achievements.builtin.__all__:
            achievement = getattr(noseachievements.achievements.builtin, name)
            self.add_achievement(achievement)

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
    default_manager = BuiltinAchievementManager
else:
    default_manager = EntryPointAchievementManager

class FilterAchievementManager(AchievementManager):
    def __init__(self, keys, manager=default_manager, default='all'):
        AchievementManager.__init__(self)
        self.include_keys = set()
        self.exclude_keys = set()
        self.add_filter(keys)
        if not self.include_keys and default is not None:
            self.add_filter(default)
        if callable(manager):
            manager = manager()
        self.manager = manager

    def add_filter(self, keys):
        if isinstance(keys, basestring):
            keys = keys.split(',')
        for key in keys:
            if key.startswith('-'):
                self.exclude_keys.add(key[1:])
            else:
                self.include_keys.add(key)

    def load(self):
        self.manager.load()
        for achievement in self.manager:
            key = achievement.key
            group, name = key.split(':', 1)
            if ('all' in self.include_keys or key in self.include_keys or
                group in self.include_keys):
                if (key not in self.exclude_keys and
                    group not in self.exclude_keys):
                    self.add_achievement(achievement)

