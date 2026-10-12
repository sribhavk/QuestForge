"""Example tests for QuestForge. Two small tests to copy from in Lesson 12."""

import unittest

from features import core


class TestCore(unittest.TestCase):
    def test_move_follows_an_exit(self):
        data = {"rooms": {
            "entrance": {"description": "A cold entrance hall.", "exits": {"north": "library"}},
            "library": {"description": "Dusty shelves.", "exits": {"south": "entrance"}},
        }}
        self.assertEqual(core.move(data, "entrance", "north"), "library")
        self.assertEqual(core.move(data, "entrance", "west"), "entrance")

    def test_describe_returns_description(self):
        room = {"description": "A cramped kitchen.", "exits": {}}
        self.assertEqual(core.describe(room), "A cramped kitchen.")
    
    def test_neighbors(self):
        data = {"rooms": {
            "entrance": {"description": "A cold entrance hall of grey stone.", "exits": {"north": "library", "east": "kitchen"}},
            "library": {"description": "Dusty shelves lean under old books.", "exits": {"south": "entrance"}},
            "kitchen": {"description": "A cramped kitchen smelling of woodsmoke.", "exits": {"west": "entrance"}},
            "study": {"description": "A tidy study with a locked desk drawer.", "exits": {}},
        }}
        self.assertEqual(core.neighbors(data, "entrance"), ["library", "kitchen"])
        self.assertEqual(core.neighbors(data, "study"), [])
        self.assertEqual(core.neighbors(data, "kitchen"), ["entrance"])

if __name__ == "__main__":
    unittest.main()
