import unittest
from document_string import *
import string
import random

class DocumentTests(unittest.TestCase):
    def setUp(self):
        self.string_x = "hi amr is here, it's test dummy"
        self.string_y = "hi mohamed is here dummy hello from the other side"
        self.doc_x = generate(100000,5)
        self.doc_y = generate(100000,5)


    def test_simple(self):
        self.x = (doc_string(self.string_y, self.string_x))


    def test_time_doc(self):
        self.x = (doc_string(self.doc_x, self.doc_y))

def generate(length,word_size):
    """
    return a string of len = (length) and each word in len random.randint(1,word_size) 
    """
    my_string = ''
    for i in range(length):
        word = ''
        for i in range(random.randint(1,word_size)):
            word += string.ascii_letters[random.randint(0,len(string.ascii_lowercase)-1)]
        my_string +=  "%s "%(word)
    return my_string


if __name__ == '__main__':
    unittest.main()