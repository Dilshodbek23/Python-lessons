import unittest
from even_num import even_n
    
class NameTest(unittest.TestCase):
    def test_even_n(self):
        formatted_name = even_n([2, 3, 4, 5, 7, 10, 12])
        self.assertEqual(formatted_name, [2, 4, 10, 12])
        
unittest.main()
