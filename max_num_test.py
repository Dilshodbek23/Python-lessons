import unittest
from max_num import max_num_
    
class NameTest(unittest.TestCase):
    def test_max_num_(self):
        formatted_name = max_num_(5, 7, 6)
        self.assertEqual(formatted_name, 7)
        
unittest.main()
