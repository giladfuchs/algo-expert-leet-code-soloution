from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i:int, cur:List[int], total:int)->None:
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)

        dfs(0, [], 0)
        return res


# print(Solution().combinationSum(candidates=
# [2,7,6,3,5,1],target=9))
print(Solution().combinationSum(candidates=[2,3,5],target=8))
print(Solution().combinationSum(candidates=[2,3,6,7],target=7))