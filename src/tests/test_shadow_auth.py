import unittest


class TestHashGeneration(unittest.TestCase):

    def test_known_hash(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")


if __name__ == '__main__':
    unittest.main()