Installation
------------
From the source repository:

    $ pip install  pip install git+git://github.com/exogen/nose-achievements.git

See [INSTALL][] for more options.

Usage
-----
### nose
Run like so:

    $ nosetests --with-achievements

Or enable it in `setup.cfg`:

    [nosetests]
    with-achievements=1

### unittest
Use the included test runner:

    from noseachievements.runner import AchievementsTestRunner
    
    unittest.main(testRunner=AchievementsTestRunner)

### Django 1.2+
Define `TEST_RUNNER` in `settings.py`:

    TEST_RUNNER = 'noseachievements.djangotest.AchievementsDjangoTestSuiteRunner'

Achievements
------------
See the list of achievements on [the homepage][home].

[INSTALL]: http://github.com/exogen/nose-achievements/blob/master/INSTALL
[home]: http://exogen.github.com/nose-achievements/
