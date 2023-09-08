import functools, collections


def majorityElement(array: list):
    # Write your code here.
    elements = functools.reduce(lambda x, y: {**x, y: x.get(y, 0) + 1}, array, {})
    most_common = max(list(elements.values()))
    peak_index = list(elements.values()).index(most_common)
    return list(elements.keys())[peak_index]


print(majorityElement([1, 2, 3, 2, 2, 1, 2]))
