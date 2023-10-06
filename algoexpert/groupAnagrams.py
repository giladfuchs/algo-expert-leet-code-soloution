from collections import defaultdict, Counter


def groupAnagrams(words):
    res = defaultdict(list)
    for word in words:
        sort_word = frozenset(Counter(word).items())
        res[sort_word].append(word)
    return list(res.values())
if __name__ == '__main__':
    print(groupAnagrams(["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]))