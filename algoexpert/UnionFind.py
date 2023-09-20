class UnionFind:
    def __init__(self):
        # Write your code here
        self.sets = {}

    def createSet(self, value):
        # Write your code here
        self.sets[value] = value

    def find(self, value):
        if value not in self.sets:
            return None
        while value != self.sets.get(value):
            value = self.sets.get(value)
        return value

    def union(self, valueOne, valueTwo):
        if self.sets.get(valueOne) is not None and self.sets.get(valueTwo) is not None:
            first = self.find(valueOne)
            second = self.find(valueTwo)
            self.sets[first] = second


if __name__ == '__main__':
    un = UnionFind()
    test = [
        {
            "arguments": [0],
            "method": "createSet",
            "output": None
        },
        {
            "arguments": [2],
            "method": "createSet",
            "output": None
        },
        {
            "arguments": [0, 2],
            "method": "union",
            "output": None
        },
        {
            "arguments": [3],
            "method": "createSet",
            "output": None
        },
        {
            "arguments": [1],
            "method": "createSet",
            "output": None
        },
        {
            "arguments": [1, 3],
            "method": "union",
            "output": None
        },
        {
            "arguments": [0],
            "method": "find",
            "output": 0
        },
        {
            "arguments": [1],
            "method": "find",
            "output": 1
        },
        {
            "arguments": [2],
            "method": "find",
            "output": 0
        },
        {
            "arguments": [3],
            "method": "find",
            "output": 1
        },
        {
            "arguments": [3, 0],
            "method": "union",
            "output": None
        },
        {
            "arguments": [0],
            "method": "find",
            "output": 1
        },
        {
            "arguments": [1],
            "method": "find",
            "output": 1
        },
        {
            "arguments": [2],
            "method": "find",
            "output": 1
        },
        {
            "arguments": [3],
            "method": "find",
            "output": 1
        }
    ]
    for _ in test:
        print(getattr(un, _.get("method"))(*_.get("arguments")), _.get('output'))
