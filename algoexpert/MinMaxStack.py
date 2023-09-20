# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.st = []
        self.min_st = []
        self.max_st = []

    def peek(self):
        if self.st:
            return self.st[-1]

    def pop(self):

        if self.st:
            val = self.st.pop()
            if self.min_st and val == self.min_st[-1]:
                self.min_st.pop()
            if self.max_st and val == self.max_st[-1]:
                self.max_st.pop()
            return val

    def push(self, number):
        if not self.min_st:
            self.min_st.append(number)
        elif number <= self.min_st[-1]:
            self.min_st.append(number)

        if not self.max_st:
            self.max_st.append(number)
        elif number >= self.max_st[-1]:
            self.max_st.append(number)

        self.st.append(number)

    def getMin(self):
        if self.min_st:
            return self.min_st[-1]

    def getMax(self):
        if self.max_st:
            return self.max_st[-1]


if __name__ == '__main__':
    un = MinMaxStack()
    test = [
        {
            "arguments": [5],
            "method": "push",
            "output": None
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 5
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 5
        },
        {
            "arguments": [5],
            "method": "push",
            "output": None
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 5
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 5
        },
        {
            "arguments": [5],
            "method": "push",
            "output": None
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 5
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 5
        },
        {
            "arguments": [5],
            "method": "push",
            "output": None
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 5
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 5
        },
        {
            "arguments": [8],
            "method": "push",
            "output": None
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 8
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 8
        },
        {
            "arguments": [8],
            "method": "push",
            "output": None
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 8
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 8
        },
        {
            "arguments": [0],
            "method": "push",
            "output": None
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 0
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 8
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 0
        },
        {
            "arguments": [8],
            "method": "push",
            "output": None
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 0
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 8
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 8
        },
        {
            "arguments": [9],
            "method": "push",
            "output": None
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 0
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 9
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 9
        },
        {
            "arguments": [5],
            "method": "push",
            "output": None
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 0
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 9
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 5
        },
        {
            "arguments": [],
            "method": "pop",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 0
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 9
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 9
        },
        {
            "arguments": [],
            "method": "pop",
            "output": 9
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 0
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 8
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 8
        },
        {
            "arguments": [],
            "method": "pop",
            "output": 8
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 0
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 8
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 0
        },
        {
            "arguments": [],
            "method": "pop",
            "output": 0
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 8
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 8
        },
        {
            "arguments": [],
            "method": "pop",
            "output": 8
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 8
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 8
        },
        {
            "arguments": [],
            "method": "pop",
            "output": 8
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 5
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 5
        },
        {
            "arguments": [],
            "method": "pop",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 5
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 5
        },
        {
            "arguments": [],
            "method": "pop",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 5
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 5
        },
        {
            "arguments": [],
            "method": "pop",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMin",
            "output": 5
        },
        {
            "arguments": [],
            "method": "getMax",
            "output": 5
        },
        {
            "arguments": [],
            "method": "peek",
            "output": 5
        },
        {
            "arguments": [],
            "method": "pop",
            "output": 5
        }
    ]
    for i, _ in enumerate(test):
        if _.get("arguments"):
            res = getattr(un, _.get("method"))(*_.get("arguments")), _.get('output')
        else:
            res = getattr(un, _.get("method"))(), _.get('output')
        print(res)
