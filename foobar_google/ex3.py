from collections import deque


def solution(map):
    n, m = len(map), len(map[0])

    def calc(x, y):
        board = [[None for _ in range(m)] for _ in range(n)]
        board[x][y] = 1
        dq = deque([(x, y)])
        while dq:
            x, y = dq.popleft()
            for x1, y1 in [[0, -1], [1, 0], [-1, 0], [0, 1]]:
                x1, y1 = x1 + x, y1 + y
                if 0 <= x1 < n and 0 <= y1 < m:
                    if board[x1][y1] is None:
                        board[x1][y1] = board[x][y] + 1
                        if map[x1][y1] == 1:
                            continue
                        dq.append((x1, y1))

        return board

    start = calc(0, 0)
    end = calc(n - 1, m - 1)
    res = float('inf')
    for i in range(n):
        for j in range(m):
            if start[i][j] and end[i][j]:
                res = min(res, start[i][j] + end[i][j] - 1)
    return res


maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]]  # Answer 11
print(solution(maze))
