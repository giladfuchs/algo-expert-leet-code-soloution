import collections
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for i, j in adjacentPairs:
            graph[i].add(j)
            graph[j].add(i)
        ans = []
        for node, adj in graph.items():
            if len(adj) == 1:
                ans.append(node)
                break
        node = ans[-1]
        while graph[node]:
            to_add = graph[node].pop()
            ans.append(to_add)
            graph[to_add].remove(node)
            node = to_add
        return ans


print(Solution().restoreArray([[4, -10], [-1, 3], [4, -3], [-3, 3]]))
# print(Solution().restoreArray([[2, 1], [3, 4], [3, 2]]))
# print(Solution().restoreArray([[4,-2],[1,4],[-3,1]]))
# print(Solution().restoreArray([[100000,-100000]]))
