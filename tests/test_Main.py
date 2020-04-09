import unittest
from Main import getStatus_message 


class Testgeturl(unittest.TestCase):
    def test_url(self):

        result = getStatus_message()
        self.assertEqual(result, "Missing status_message in the response data")

if __name__=='__main__':
    unittest.main()

