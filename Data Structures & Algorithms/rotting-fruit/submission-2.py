class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        number_of_rows = len(grid)
        number_of_columns = len(grid[0])
        for i in range(number_of_rows):
            for j in range(number_of_columns):
                if grid[i][j]==2:
                    queue.append((i,j))
        directions = [(-1,0),(1,0),(0,-1),(0,1)] # up, down, left, right
        number_of_minutes = 0
        while(queue):
            number_of_rotten_fruit = len(queue)
            for _ in range(number_of_rotten_fruit):
                i,j  = queue.pop(0)
                for coord in directions:
                    delta_x,delta_y = coord 
                    if (i+delta_x)<0 or (i+delta_x)>=number_of_rows:
                        continue
                    if (j+delta_y)<0 or (j+delta_y)>=number_of_columns:
                        continue
                    if grid[i+delta_x][j+delta_y]==1:
                        grid[i+delta_x][j+delta_y]=2
                        queue.append((i+delta_x,j+delta_y))
            if(queue):
                number_of_minutes+=1
        for i in range(number_of_rows):
            for j in range(number_of_columns):
                if grid[i][j]==1:
                    return -1
        return number_of_minutes
            
