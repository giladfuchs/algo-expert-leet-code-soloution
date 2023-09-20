def hasSingleCycle(array):
    n = len(array)
    ans = False
    i = 0
    while i < n:
        visited = [0] * n
        curr = i
        for _ in range(n):
            curr += array[curr]
            curr = curr % n
            visited[curr] += 1
        if all(ele == 1 for ele in visited):
            return True
        i += 1
    return ans


if __name__ == '__main__':
    print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
