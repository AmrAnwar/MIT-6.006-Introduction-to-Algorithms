import unittest
from fibonacci_with_memory import *
from datetime import datetime


class DocumentTests(unittest.TestCase):
    def setUp(self):
        self.end = 50
        
    def test_fab(self):
        tick = datetime.now()
        for i in range(1,self.end):
            rr= fab(i)
        tock = datetime.now()   
        diff = tock - tick 
        print("Take Time %s" %(diff.total_seconds()))


    def test_fab_with_memory(self):
        tick = datetime.now()
        for i in range(1,self.end):
            rr= fab_memory(i) 
        tock = datetime.now()   
        diff = tock - tick 
        print("Take Time %s" %(diff.total_seconds()))

if __name__ == '__main__':
    unittest.main()