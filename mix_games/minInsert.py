from heapq import heapify, heappush, heappop


class MinInsert:

    def __init__(self):
        self.arr = [None] * 1000
        self.heap = []
        heapify(self.heap)
        heappush(self.heap, 0)

    def insert(self, number):
        index = heappop(self.heap)
        self.arr[index] = number
        if not self.heap:
            heappush(self.heap, index + 1)

    def remove(self, index):
        if self.arr[index] is None:
            return False
        self.arr[index] = None
        heappush(self.heap, index)

        return True


def sublists(lst):
    n = len(lst)
    sublists = []

    for start in range(n):
        for end in range(start + 1, n + 1):
            sublists.append(sum(lst[start:end]))

    return sublists


original_list = [1, 2, 3]
sublists_nested = sublists(original_list)
print(sublists_nested)
if __name__ == '__main__':
    from random import randint

    mn = MinInsert()
    for i in range(999):
        mn.insert(randint(1, 554))

    mn.remove(13)
    mn.insert(324)
    mn.remove(11)
    mn.insert(324)
