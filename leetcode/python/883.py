from typing import List
# import numpy as np

class Solution:

    def projectionArea(self, grid: List[List[int]]) -> int:
        # top view
        top_view_area = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                # top_view_area = max(grid[i][j], top_view_area)
                if grid[i][j] > 0:
                    top_view_area += 1
        # print(top_view_area)

        # xz view 
        xz_view_area = 0
        for i in range(len(grid)):
            tower = grid[i]
            xz_view_area += max(tower)

        # print(xz_view_area)
        
        # yz view
        yz_view_area = 0
        for j in range(len(grid)):
            max_col_height = 0
            for i in range(len(grid)):
                max_col_height  = max(max_col_height, grid[i][j])
            yz_view_area += max_col_height

        # print(yz_view_area)
        ans = top_view_area + xz_view_area + yz_view_area
        return ans

sol = Solution()

# grid = [[1,2],[3,4]]
# grid = [[1,0],[0,2]] 

grid = [[2]]

print(sol.projectionArea(grid))