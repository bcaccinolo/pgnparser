import unittest
from move import Move

class TestMove(unittest.TestCase):

    def test_init(self):
        m = Move()
        m.white = 'e4'

    def test_dump(self):
        m = Move()
        m.id = 1
        m.white = 'e4'
        m.black = 'd5'
        self.assertEqual(m.dump(), '1. e4 d5')
