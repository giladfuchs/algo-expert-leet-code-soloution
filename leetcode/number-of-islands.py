from typing import List

water = '0'
island = '1'


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def make_water(i, j):
            if i<0 or j<0 or i==len(grid) or j ==len(grid[0]):
                return
            elif  grid[i][j]==water:
                return
            else:
                grid[i][j] = water

            make_water(i+1,j)
            make_water(i-1,j)
            make_water(i,j+1)
            make_water(i,j-1)
        for i, line in enumerate(grid):
            for j, _ in enumerate(line):
                if  _ == island:
                    count+=1
                make_water(i,j)

        return count

print(Solution().numIslands( grid =[["1","0","1","1","0","1","1"]]))
print(Solution().numIslands( grid =[["1","1","0","0","0"],
                                    ["1","1","0","0","0"],
                                    ["0","0","1","0","0"],
                                    ["0","0","0","1","1"]]))
print(Solution().numIslands( grid =
[["1","1","1"],
 ["1","0","1"],
 ["1","1","1"]]))