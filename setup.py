from setuptools import setup

setup(
    name='nose-achievements',
    version='0.1',
    packages=['noseachievements'],
    install_requires=['nose>=0.11'],
    author="Brian Beck",
    author_email='exogen@gmail.com',
    entry_points={
        'nose.plugins.0.10': [
            'achievements = noseachievements.plugin:Achievements'],
        'nose.achievements': [
            'instant-feedback = noseachievements.achievements.speed:InstantFeedback',
            'coffee-break = noseachievements.achievements.speed:CoffeeBreak',
            'take-a-walk = noseachievements.achievements.speed:Walk',
            'take-a-nap = noseachievements.achievements.speed:Nap',
            'take-a-vacation = noseachievements.achievements.speed:Vacation',
            'anticipation = noseachievements.achievements.speed:Anticipation',
            'night-shift = noseachievements.achievements.time:NightShift',
            'punctuality = noseachievements.achievements.time:Punctuality',
            'complete-failure = noseachievements.achievements.failure:CompleteFailure',
            'epic-fail = noseachievements.achievements.failure:EpicFail',
            'minor-letdown = noseachievements.achievements.failure:MinorLetdown',
            'my-god-its-full-of-dots = noseachievements.achievements.size:FullOfDots',
            'are-you-mocking-me = noseachievements.achievements.libraries:MockingMe']}
)

