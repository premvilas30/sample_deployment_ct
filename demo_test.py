import demo
import unittest

class Demotest(unittest.TestCase):

    def setUp(self):
        self.app = demo.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_message(self):
        response = self.app.get('/')
        message = 'sample application'
        assert b'sample application' in response.data

if __name__ == '__main__':
    unittest.main()


