class Solution:
    def dfs(self,grid,i,j,visited):
        if grid[i][j]==0:
            return
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        ROWS = len(grid)
        COLS = len(grid[0])
        visited.add((i,j))
        for x,y in directions:
            delta_x = i+x
            delta_y = j+y 
            if delta_x>=0 and delta_x<ROWS and delta_y>=0 and delta_y<COLS: # valid coordinate
                if ((delta_x,delta_y) not in visited):
                    self.dfs(grid,delta_x,delta_y,visited)
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        visited_global = set()
        visited_all = set()
        for i in range(ROWS):
            for j in range(COLS):
                visited = set()
                if grid[i][j]==1:
                    if ((i,j) not in visited_global):
                        self.dfs(grid,i,j,visited)
                        visited_l = list(visited)
                        visited_l = [(row-i,col-j) for row,col in visited_l]
                        visited_l.sort()
                        visited_all.add(tuple(visited_l))
                        visited_global = visited | visited_global
        print(visited_all)
        return len(visited_all)


        