from setuptools import setup

setup(
    name='nose-achivements',
    version='0.1',
    packages=['noseachievements'],
    install_requires=['nose>=0.11'],
    author="Brian Beck",
    author_email='exogen@gmail.com',
    entry_points={
        'nose.plugins.0.10': [
            'achievements = noseachievements.plugin:Achievements'],
        'nose.achievements': [
            'mocking-me = noseachievements.achievements:MockingMe',
            'night-shift = noseachievements.achievements:NightShift']}
)

