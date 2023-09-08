from functools import reduce
from collections import Counter


def levenshteinDistance(str1, str2):
    counter1, counter2 = Counter(str1), Counter(str2)
    not_in_1 = 0
    not_in_2 = 0
    common = 0
    for c, count in counter1.items():
        count_c2 = counter2.get(c)
        if count_c2 is None:
            not_in_2 += count
            continue
        counter2.pop(c)
        if count_c2 >= count:
            common += count
            if count_c2 > count:
                not_in_1 += (count_c2 - count)

        elif count_c2 < count:
            common += count_c2
            not_in_2 += (count - count_c2)
    n_sum = sum(list(counter2.values()))
    not_in_1 += n_sum
    mmin = min(not_in_2, not_in_1)
    mmixxn = max(not_in_2, not_in_1)

    ans = mmin + (mmixxn - mmin)
    print(ans)
    return ans


def sol(st1, st2):
    edits = [[x for x in range(len(st1) + 1)] for y in range(len(st2) + 1)]
    for i in range(1, len(st2) + 1):
        edits[i][0] = edits[i - 1][0] + 1
    for i in range(1, len(st2) + 1):
        for j in range(1, len(st1) + 1):
            edits[i][j] = edits[i - 1][j - 1] if st2[i - 1] == st1[j - 1] else \
                min( edits[i - 1][j - 1], edits[i][j - 1], edits[i - 1][j]) + 1

    print(edits[-1][-1])
    return edits[-1][-1]


# d = reduce(lambda x, y: {**x, y: x.get(y, 0) + 1}, commands, {_: 0 for _ in ['D', 'U']})
sstr = "abc"
st23 = "yabd"
sol(sstr, st23)
# d = reduce(lambda x, y: {**x, y: x.get(y, 0) + 1}, commands, {_: 0 for _ in ['D', 'U']})
sstr = "biting"
st23 = "mitten"
sol(sstr, st23)
