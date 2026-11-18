class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        maxArea = 0 
        def dfs(i,j,visited):
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            visited.add((i,j))
            area = 1
            for x,y in directions:
                delta_x = i+x
                delta_y =j+y
                if delta_x>=0 and delta_x<ROWS and delta_y>=0 and delta_y<COLS:
                    if grid[delta_x][delta_y]==1:
                        if ((delta_x,delta_y) not in visited):
                            area+=dfs(delta_x,delta_y,visited)
            return area
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    if ((i,j) not in visited):
                        maxArea = max(dfs(i,j,visited),maxArea)
        return maxArea
        

        