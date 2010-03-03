Unit Testing Achevements
========================
by [Brian Beck][www] / [@ua6oxa](http://twitter.com/ua6oxa)

![trophy](http://exogen.github.com/nose-achievements/images/trophy.png)

* Unlock achievements for running your test suite!
* Works with nose, unittest, and Django
* Tested with Python 2.6 and 3.1
* Entry points for discovering more achievements

__[See the list of achievements on the homepage][home]__

Installation
------------
From the source repository:

    $ pip install git+git://github.com/exogen/nose-achievements.git

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

More Ideas
----------
Please share your achievement ideas on the [wiki][]!

[INSTALL]: http://github.com/exogen/nose-achievements/blob/master/INSTALL
[home]: http://exogen.github.com/nose-achievements/
[wiki]: http://wiki.github.com/exogen/nose-achievements/
[www]: http://brianbeck.com/
