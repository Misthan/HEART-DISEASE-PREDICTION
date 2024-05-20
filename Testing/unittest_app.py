import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_route(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)


    def test_register_route(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_predict_route(self):
        response = self.app.get('/predict')
        self.assertEqual(response.status_code, 405)

    def test_logout_route(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302)

    def test_user_route(self):
        response = self.app.get('/user')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()