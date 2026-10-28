class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]],number_of_rows:int,number_of_columns:int,x:int,y:int):
            if x<0 or x>=number_of_rows or y<0 or y>=number_of_columns or grid[x][y]=='0': # culling searches that are not feasible
                return 
            #mark it as visited 
            grid[x][y] = '0'
            directions = [(1,0),(-1,0),(0,1),(0,-1)] # down, up, right, left 
            for coord in directions:
                delta_x,delta_y = coord
                dfs(grid,number_of_rows,number_of_columns,x+delta_x,y+delta_y)
            return
            

        total_number_of_islands = 0 
        if not grid:
            return total_number_of_islands
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        for i in range(0,number_of_rows):
            for j in range(0,number_of_columns):
                if grid[i][j]=='1':
                    total_number_of_islands+=1
                    dfs(grid,number_of_rows,number_of_columns,i,j)
        return total_number_of_islands


        