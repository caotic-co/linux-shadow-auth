import unittest

from pam_linux.functions import return_true

class TestHashGeneration(unittest.TestCase):

    def test_known_hash(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_true(self):
        self.assertFalse(return_true(), "Should be True")


if __name__ == '__main__':
    unittest.main()