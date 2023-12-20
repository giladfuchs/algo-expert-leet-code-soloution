from collections import OrderedDict


class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.lru = OrderedDict()

    def insertKeyValuePair(self, key, value):
        if key in self.lru:
            self.lru.move_to_end(key)
        else:
            self.lru[key] = value
        if len(self.lru) > self.maxSize:
            self.lru.popitem(last=False)

    def getValueFromKey(self, key):
        # Write your code here.

        return self.lru.get(key)

    def getMostRecentKey(self):
        # Write your code here.
        return list(self.lru.keys())[-1]


result = OrderedDict()
result['c'] = 3
result['b'] = 2
result['a'] = 1
result.popitem(last=False)
print(len(result), list(result.values())[-1])
