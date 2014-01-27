import unittest
from move import Move

class TestMove(unittest.TestCase):

    def test_init(self):
        m = Move()
        m.white = 'e4'

    def test_dump(self):
        m = Move()
        m.white = 'e4'
        self.assertEqual(m.dump(), '1. e4 d5')
