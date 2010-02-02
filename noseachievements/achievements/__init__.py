import logging


log = logging.getLogger(__name__)
ENTRY_POINT = 'nose.achievements'

class AchievementError(Exception):
    pass

class AchievementNotFound(AchievementError):
    pass

class LoadAchievementError(AchievementError):
    pass

def get_achievement(name):
    from pkg_resources import iter_entry_points
    load_error = None
    for entry_point in iter_entry_points(ENTRY_POINT, name):
        try:
            achievement = load_achievement(entry_point)
        except ImportError, e:
            log.error("Could not load entry point %r", entry_point.name)
            load_error = e
        else:
            return achievement
    if load_error is not None:
        raise LoadAchievementError(load_error)
    else:
        raise AchievementNotFound(name)

def get_achievements(raise_on_error=False):
    from pkg_resources import iter_entry_points
    for entry_point in iter_entry_points(ENTRY_POINT):
        try:
            achievement = load_achievement(entry_point)
        except ImportError, e:
            log.error("Could not load entry point %r", entry_point.name)
            if raise_on_error:
                raise LoadAchievementError(e)
        else:
            yield achievement

def load_achievement(entry_point):
    achievement = entry_point.load()
    if not hasattr(achievement, 'key'):
        achievement.key = entry_point.name
    return achievement

