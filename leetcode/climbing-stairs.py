import functools
from typing import List

from collections import OrderedDict
class Solution:
    def fibb(self, n: int) -> int:
        if n in [1,2]:
            return n + 1

        return self.fibb(n-1) + self.fibb(n-2)

    def climbStairs(self, n: int) -> int:
        return self.fibb(n+1) if n>3 else n

    def lastStoneWeight(self, stones: List[int]) -> int:
        weight = functools.reduce(lambda x,y: {**x,  y:x.get(y,0) + 1},stones, {})
        
        weight_keys = sorted(list(weight.keys()))
        def remove_key(index):
            weight[index] -= 1
            if not weight[index]:
                del weight[index]

        while len(weight_keys) > 1:
            y =  weight_keys[-1]
            remove_key(y)
            x = y if weight.get(y) else weight_keys[-2]
            remove_key(x)

            if x!=y:
                y = y-x
                if y in weight.keys():
                    weight[y] += 1
                else:
                    weight[y] = 1
            weight_keys = sorted(list(weight.keys()))

        return weight_keys[0] if weight_keys  and weight[weight_keys[0]]%2 ==1 else 0

print(Solution().climbStairs(4))
# print(Solution().lastStoneWeight([2,2]))
# print(Solution().lastStoneWeight([2,7,4,1,8,1]))
print(Solution().lastStoneWeight(
[10,4,2,10]

))