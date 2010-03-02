import unittest
from datetime import datetime
from cStringIO import StringIO
from cPickle import dump, load

from noseachievements.data import AchievementData


class TestAchievementData(unittest.TestCase):
    def setUp(self):
        self.data = AchievementData({'time.start': datetime.now(),
                                     'time.finish': datetime.now()})
        self.stream = StringIO()
        self.data.save(self.stream)
        self.stream.seek(0)

    def test_is_dict(self):
        self.assert_(isinstance(self.data, dict))

    def test_save_writes_data_to_stream(self):
        stream = StringIO()
        dump(self.data, stream, AchievementData.PICKLE_PROTOCOL)
        self.assertEqual(self.stream.getvalue(), stream.getvalue())

    def test_load_reads_data_from_stream(self):
        data = AchievementData.load(self.stream)
        self.assertEqual(self.data, data)

class TestAchievementDataFromEmptyFile(unittest.TestCase):
    def setUp(self):
        self.stream = StringIO()

    def test_load_returns_empty_data_instead_of_eof_error(self):
        data = AchievementData.load(self.stream)
        self.assertEqual(data, AchievementData())

