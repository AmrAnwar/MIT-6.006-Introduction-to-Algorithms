"""
we don't need to implement it cause it was written in python before
check this(source code) : https://github.com/python/cpython/blob/2.7/Lib/heapq.py
docs : https://docs.python.org/2/library/heapq.html
"""

"""
8.4.1. Basic Examples from Docs
"""
from heapq import heappush,heappop
def heapsort(iterable):
	h = []
	for value in iterable:
		heappush(h, value)
	return [heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])