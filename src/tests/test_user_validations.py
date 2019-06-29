import unittest
import os
import sys
import subprocess
import shadow_auth
from ast import literal_eval


class TestUserValidations(unittest.TestCase):
    """Test cases for user validation"""

    # Required to obtain always the same hash in the tests
    os.environ['PYTHONHASHSEED'] = "0"

    def test_validate_root(self):
        """Validate that the expected results when the root user is disabled"""

        self.assertFalse(shadow_auth.validate_with_password("root", "1234"))
        self.assertFalse(shadow_auth.validate_with_hash("root", "$6$AbdTEGdsa"))
        self.assertFalse(shadow_auth.validate_with_hash("root", "$6$AbdTEGdsa"))
        self.assertFalse(shadow_auth.validate_with_hash("root", "AbdTEGdsa"))
        self.assertFalse(shadow_auth.validate_with_hash("root", "$6$AbdTEGds$agsdgsdtSHSHFKSjsghdy"))

        password_str_info = subprocess.check_output(
            [sys.executable, '-c', 'import shadow_auth;print(shadow_auth.get_password_info("root"))']
        ).decode("utf-8")

        password_info = literal_eval(password_str_info)

        self.assertEqual(
            "6",
            password_info["algorithm"],
            "The algorithm should be SHA-256 if the root user is disabled"
        )

        self.assertEqual(
            "hjIIfGAE",
            password_info["salt"],
            "The expected salt does not match, maybe the root user is enabled"
         )


if __name__ == '__main__':
    unittest.main()
