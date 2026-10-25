import unittest

from features import reports

class TestReports(unittest.TestCase):
    def test_average_rooms(self):
        self.assertEqual(reports.average_rooms({"history": [4, 5, 6]}), 5)
    
    def test_average_rooms_empty(self):
        self.assertEqual(reports.average_rooms({"history": []}), 0)

if __name__ == "__main__":
    unittest.main()