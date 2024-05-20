import unittest
from app import app


class RegressionTesting(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        app.config['TESTING'] = False


    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Heart Disease Prediction System | Homepage', response.data)

    def test_login_form(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)


    def test_register_form(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'register', response.data)

    def test_logout_route(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302)  # 302 for redirection
        self.assertIn(b'Redirecting', response.data)




    def test_predict_route(self):
        response = self.app.post('/predict', data=dict(
            Age=52,
            sex=1,
            chestPainTypes=0,
            trestBps=125,
            SerumCholesterol=212,
            FastingBloodSugar=0,
            ecg_results=1,
            MaximumHeartRate=168,
            exercise_angina=0,
            stDepression=1,
            st_slope=2,
            major_vessels=2,
            thalassemia=3
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'predict', response.data)







if __name__ == '__main__':
    unittest.main()