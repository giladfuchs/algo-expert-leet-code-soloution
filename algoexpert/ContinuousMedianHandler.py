# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
from heapq import heapify, heappush, heappop
import bisect

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.sort_array = []

    def insert(self, number):
        # Write your code here.
        bisect.insort(self.sort_array, number)
        size = len(self.sort_array)
        is_odd = size & 1
        med = size // 2
        self.median = self.sort_array[med + 1] if is_odd else \
            (self.sort_array[med + 1] + self.sort_array[med]) / 2

    def getMedian(self):
        return self.median


if __name__ == '__main__':
    heap = ContinuousMedianHandler()
    bisect.insort(heap, 3)
    bisect.insort(heap, 2)
    bisect.insort(heap, 5)
    bisect.insort(heap, 1)
    bisect.insort(heap, 9)
    bisect.insort(heap, 6)
    print(heap)
