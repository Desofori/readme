import unittest
import pyotp
from key_management import generate_user_key, generate_user_secret, authenticate_user, store_user_password

class TestKeyManagement(unittest.TestCase):
    def test_generate_user_key(self):
        username = "test_user"
        key = generate_user_key(username)
        self.assertIsNotNone(key)

    def test_generate_user_secret(self):
        username = "test_user"
        secret = generate_user_secret(username)
        self.assertIsNotNone(secret)

    def test_authenticate_user(self):
        username = "test_user"
        password = "password"
        store_user_password(username, password)
        secret = generate_user_secret(username)
        totp = pyotp.TOTP(secret).now()
        self.assertTrue(authenticate_user(username, password, totp))

if __name__ == '__main__':
    unittest.main()
