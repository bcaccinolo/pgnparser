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

    def test_validate_format(self):
        m = Move()
        moveOK = '1. e4 { comment }'
        moveKO = 'a. 11 '
        self.assertNotEqual(m.validate_format(moveOK), None)
        self.assertEqual(m.validate_format(moveKO), None)

    def test_parse(self):
        move1 = '1. e4 { comment }'
        m = Move()
        m.parse(move1)
        self.assertEqual(m.dump(), move1)

