'''
200. Number of Islands
Solved
Medium
Topics
conpanies icon
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''

from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        move = [(1,0),(0,1),(-1,0),(0,-1)]
        mRow, mCol = len(grid),len(grid[0])
        res = 0

        def bfs(n:tuple):

            q = deque()
            q.append(n)

            nonlocal mRow
            nonlocal mCol

            while q:
                r,c = q.popleft()
                print(r,c)
                for vert,horz in move:
                    r2,c2 = r+vert, c+horz

                    if r2 >= mRow or c2 >= mCol or r2 < 0 or c2 < 0 or grid[r2][c2] == "0":
                        continue
                    #print(r2,c2)
                    q.append((r2,c2))
                    grid[r2][c2] = "0"
        
        for r in range(mRow):
            for c in range(mCol):
                if grid[r][c] == "1":
                    res += 1
                    bfs((r,c))

        return res