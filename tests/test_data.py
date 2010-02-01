import unittest
from cPickle import dump
from cStringIO import StringIO
from datetime import datetime
from noseachievements.data import AchievementData


class TestAchievementData(unittest.TestCase):
    def setUp(self):
        self.stream = StringIO()
        self.data = AchievementData({'time.start': datetime.now(),
                                     'time.finish': datetime.now()})
        self.data.save(self.stream)

    def tearDown(self):
        self.stream.truncate(0)

    def test_writes_to_stream(self):
        stream = StringIO()
        dump(dict(self.data), stream, protocol=2)
        self.assertEqual(self.stream.getvalue(), stream.getvalue())

    def test_reads_from_stream(self):
        stream = StringIO()
        dump(dict(self.data), stream, protocol=2)
        stream.seek(0)
        data = AchievementData.load(stream)
        self.assertEqual(data, self.data)

