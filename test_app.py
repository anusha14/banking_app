import unittest

from banking_system import app
from banking_system.models import db


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def register_user(self, name="sri", password="test1234", balance=200):
        user_data = {'name': name, 'password': password, 'balance': balance}
        return self.app.post('/create_account', data=user_data, follow_redirects=True)

    def login_user(self, id=1, password="test1234"):
        user_data = {'id': id, 'password': password}
        return self.app.post('/login', data=user_data)

    def test_user_registration(self):
        user_multiple_registration = self.register_user()
        self.assertIn(b'sri', user_multiple_registration.data)
        self.assertEqual(user_multiple_registration.status_code, 200)

    def test_user_login(self):
        self.register_user()
        login_res = self.login_user()
        self.assertEqual(login_res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
