from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel.insert(0, 0)
        total = 0
        for type_garbage in ['G', 'P', 'M']:
            temp_add = 0
            for i, st in enumerate(garbage):
                count = st.count(type_garbage)
                if count > 0:
                    total += count + travel[i ] + temp_add
                    temp_add = 0
                else:
                    temp_add += travel[i ]

        return total


print(Solution().garbageCollection(["G", "P", "GP", "GG"], [2, 4, 3]))
