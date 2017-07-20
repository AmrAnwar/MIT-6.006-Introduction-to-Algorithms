import unittest
from document_string import *

class DocumentTests(unittest.TestCase):
    def setUp(self):
        self.doc_x = "hi there it's amr , hi"
        self.doc_y = "hi there it's , hi"
        
    def test_creation(self):
        self.assertEqual( int(doc_string(self.doc_x, self.doc_y)) ,20 )

        # self.assertIn(doc_string(self.doc_x, self.doc_y), range(20, 21))
        
            
if __name__ == '__main__':
    unittest.main()