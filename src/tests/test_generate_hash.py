import unittest
import shadow_auth


class TestHashGeneration(unittest.TestCase):
    """Test cases for hash generation with openssl"""

    def test_generate_md5_hash(self):
        """Validate that the MD5 hash generation works"""

        md5_generated_hash = shadow_auth.generate_openssl_hash(
            algorithm=shadow_auth.Algorithm.MD5,
            salt="TrOIigLp",
            text="abcd12345"
        )

        self.assertEqual(
            "$1$TrOIigLp$FJg1nUqEQPt4OerLOWzr/1",
            md5_generated_hash,
            "The generated MD5 Hash does not match with the expected result"
        )

    def test_generate_sha256_hash(self):
        """Validate that the SHA-256 hash generation works"""

        sha256_generated_hash = shadow_auth.generate_openssl_hash(
            algorithm=shadow_auth.Algorithm.SHA_256,
            salt="TrOIigLp",
            text="abcd12345"
        )

        self.assertEqual(
            "$5$TrOIigLp$6usEDvu0NgyuQ/IqQyvSBoP0x2RiNOz5izrMViHwXv2",
            sha256_generated_hash,
            "The generated SHA-256 Hash does not match with the expected result"
        )

    def test_generate_sha512_hash(self):
        """Validate that the SHA-512 hash generation works"""

        sha512_generated_hash = shadow_auth.generate_openssl_hash(
            algorithm=shadow_auth.Algorithm.SHA_512,
            salt="TrOIigLp",
            text="abcd12345"
        )

        self.assertEqual(
            "$6$TrOIigLp$IU0KwZfzVkuLLy/9vMFH1RgOmqE3LAGk0K9/15WOGStkeaN2IWYkY0jzCWHMUcSnnewnt9bOUwD2vStgko79v/",
            sha512_generated_hash,
            "The generated SHA-512 Hash does not match with the expected result"
        )


if __name__ == '__main__':
    unittest.main()