from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque([])
        ff = 0
        min_min = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                elif grid[r][c] == 1:
                    ff+=1
        while q:
            r, c, dist = q.popleft()
            min_min = max(min_min, dist)
            for r1, c1 in((-1, 0), (1, 0), (0, -1), (0,1)):
                nr, nc = r + r1, c + c1
                if 0 <= nr < len(grid) and 0 <=nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, dist+1))
                    ff-=1

        if ff ==0:
          return min_min
        else:
          return -1



        
    