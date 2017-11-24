import unittest
from panel import app

class BasicTest(unittest.TestCase):
    """context manage test"""
    def setUp(self):
        self.app=app.test_client()

    def tearDown(self):
        pass

    def test_panel(self):
        """test panel status"""
        response=self.app.get('/')
        self.assertEqual(response.status_code,200,"[ERROR]status code error")


if __name__=="__main__":
    unittest.main()