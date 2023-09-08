from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = {}
        count = 0
        for _ in time:
            if 0 in ans and _%60 ==0:
                count+=ans[0]
            elif 60 - _%60 in ans:
                count+= ans[60 - _%60]

            ans[_%60] = ans.get(_%60,0) +1
        return count

print(Solution().numPairsDivisibleBy60([15,63,451,213,37,209,343,319]))
print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))
print(Solution().numPairsDivisibleBy60([60,60,60]))