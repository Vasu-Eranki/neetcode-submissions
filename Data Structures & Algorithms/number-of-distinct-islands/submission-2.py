class Solution:
    def dfs(self,grid,i,j,visited):
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)] # right,left,down,up
        visited.add((i,j))
        for x,y in directions:
            delta_x = x+i
            delta_y = y+j
            if delta_x>=0 and delta_x<ROWS and delta_y>=0 and delta_y<COLS:
                if grid[delta_x][delta_y]==1:
                    if ((delta_x,delta_y) not in visited):
                        self.dfs(grid,delta_x,delta_y,visited)
        return
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        hashmap = {}
        visited_all = set()
        visited_grid = set()
        for i in range(ROWS):
            for j in range(COLS):
                visited = set()
                if grid[i][j]==1:
                    if ((i,j) not in visited_grid):
                        self.dfs(grid,i,j,visited)
                        visited_l = list(visited)
                        visited_l = [(x-i,y-j) for x,y in visited_l]
                        visited_l.sort()
                        visited_all.add(tuple(visited_l))
                        visited_grid = visited|visited_grid
        return len(visited_all)