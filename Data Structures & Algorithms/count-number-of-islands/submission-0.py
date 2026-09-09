class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen = set()
        count = 0
        def dfs(r, c):
            seen.add((r,c)) 
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r+dr, c+dc
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr, nc) not in seen and grid[nr][nc] == "1":
                  dfs(nr, nc)

        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if (r,c) not in seen and grid[r][c] == "1":
                    count+=1
                    dfs(r,c)
        return count


        