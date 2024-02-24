class Solution:
    def numIslands(self,grid:list[list[int]])->int:

        rows = len(grid)
        cols = len(grid[0])
        result = 0
        visited = set()


        def dfs(r,c):
            if (r,c) in visited:
                return
            
            visited.add((r,c))

            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                if(nr in range(rows) and nc in range(cols) and grid[nr][nc] =='1'):
                    dfs(nr,nc)




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    result +=1

        return result
    

ss = Solution()
grid = [['1','1','0'],
        ['1','0','0'],
        ['0','1','0']
        ]

print(ss.numIslands(grid=grid))