from setuptools import setup

setup(
    name='nose-achievements',
    version='0.1',
    packages=['noseachievements'],
    install_requires=['nose>=0.11'],
    author="Brian Beck",
    author_email='exogen@gmail.com',
    entry_points="""
    [nose.plugins.0.10]
    achievements = noseachievements.plugin:AchievementsPlugin

    [nose.achievements]
    builtin:night-shift = noseachievements.achievements.builtin:NightShift
    builtin:punctuality = noseachievements.achievements.builtin:Punctuality
    builtin:instant-feedback = noseachievements.achievements.builtin:InstantFeedback
    builtin:coffee-break = noseachievements.achievements.builtin:CoffeeBreak
    builtin:take-a-walk = noseachievements.achievements.builtin:TakeAWalk
    builtin:my-god-its-full-of-dots = noseachievements.achievements.builtin:FullOfDots
    builtin:mocking-me = noseachievements.achievements.builtin:MockingMe
    builtin:great-expectations = noseachievements.achievements.builtin:GreatExpectations
    builtin:complete-failure = noseachievements.achievements.builtin:CompleteFailure
    builtin:epic-fail = noseachievements.achievements.builtin:EpicFail
    builtin:minor-letdown = noseachievements.achievements.builtin:MinorLetdown
    builtin:major-letdown = noseachievements.achievements.builtin:MajorLetdown
    builtin:happy-ending = noseachievements.achievements.builtin:HappyEnding
    builtin:to-understand-recursion = noseachievements.achievements.builtin:ToUnderstandRecursion
    builtin:take-a-nap = noseachievements.achievements.builtin:TakeANap
    builtin:take-a-vacation = noseachievements.achievements.builtin:TakeAVacation
    builtin:sausage-fingers = noseachievements.achievements.builtin:SausageFingers
    builtin:100-code-coverage = noseachievements.achievements.builtin:CodeCoverage
    """
)

