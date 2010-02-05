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
            'achievements = noseachievements.plugin:AchievementsPlugin'],
        'nose.achievements': []}
)
