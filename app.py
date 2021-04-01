from lib import utils

import unittest
 
class TestNumber(unittest.TestCase):
   def test_add(self):
       self.assertEqual(1 + 2, 3)
       self.assertEqual(2 + 2, 4)
 
   def testMultiply(self):
       self.assertEqual(1 * 1, 1)
       self.assertEqual(1 * 2, 2)
       self.assertEqual(2 * 4, 8)
       
if __name__ == "__main__":
    print('CICD')

    # try:
    #     assert utils.add(1, 1) == 2, "Should be 2"
    #     print('success')
    # except:
    #     print('error')

    unittest.main()