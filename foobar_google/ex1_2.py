def ex1(s):
    # 0-24
    # 1-23
    # 2-22
    # 11-13
    # 2
    return ''.join(chr(219 - ord(ch)) if ch.islower() else ch for ch in s)


def ex2_1(s):
    count = side = 0

    for i in s:
        if i == '>':
            side += 1
        elif i == '<':
            count += side
    return count * 2


from collections import deque

paths = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]


def get_paths(src):
    return [(src[0] + x, src[1] + y) for x, y in
            paths
            if 0 <= src[0] + x < 8 and 0 <= src[1] + y < 8
            ]


def ex2_2(src, dest):
    src = (src // 8, src % 8)
    dest = (dest // 8, dest % 8)

    q = deque([(src[0], src[1], 0)])
    visited = {src}
    while True:
        current = q.popleft()
        if current[0] == dest[0] and current[1] == dest[1]:
            return current[2]
        for x, y in get_paths((current[0], current[1])):
            if (x, y) not in visited:
                q.append((x, y, current[2] + 1))
                visited.add((x, y))


print(ex2_2(19, 36))
print(ex2_2(0, 1))
