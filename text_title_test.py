import unittest
from text_title import text_t
    
class NameTest(unittest.TestCase):
    def test_text_t(self):
        formatted_name = text_t(['book', 'pen', 'job'])
        self.assertEqual(formatted_name, ['Book', 'Pen', 'Job'])
        
unittest.main()
