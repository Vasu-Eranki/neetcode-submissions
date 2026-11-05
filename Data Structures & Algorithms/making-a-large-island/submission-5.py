class Solution:
    ROWS = 0 
    COLS = 0
    def bfs(self,grid:List[List[int]],i:int,j:int,visited:set[int],grid_id:int)->int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)] # right, left, down, up
        count = 0
        queue =[(i,j)]
        while(queue):
            length = len(queue)
            for _ in range(length):
                i,j = queue.pop(0)
                if grid[i][j]==1: # only if it is 1, we go further to mark it, values on grid can be 0/1 and grid IDs
                    grid[i][j]=grid_id
                    visited.add((i,j))
                    count+=1
                    for x,y in directions:
                        delta_x = i+x 
                        delta_y = j+y
                        if(delta_x>=0) and (delta_x<self.ROWS) and (delta_y>=0) and (delta_y<self.COLS):
                            if (delta_x,delta_y) not in visited:
                                queue.append((delta_x,delta_y))
        return count

            
            
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        self.ROWS = len(grid)
        self.COLS = len(grid[0])
        grid_ID = 2 # 0/1 are forbidden
        hashmap = {}
        visited = set()
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if(grid[i][j]==1):
                    number_of_cells = self.bfs(grid,i,j,visited,grid_ID)
                    hashmap[grid_ID] = number_of_cells
                    grid_ID+=1
        directions = [(0,1),(0,-1),(1,0),(-1,0)] # right, left, down, up
        max_cells = 0
        if hashmap:
            max_cells = max(list(hashmap.values()))
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if grid[i][j]==0:
                    islands_in_vicinity = set()
                    area = 0
                    for x,y in directions:
                        delta_x = x+i 
                        delta_y = y+j 
                        if(delta_x>=0) and (delta_x<self.ROWS) and (delta_y>=0) and (delta_y<self.COLS):
                            if grid[delta_x][delta_y]!=0:
                                islands_in_vicinity.add(grid[delta_x][delta_y])
                    for entry in islands_in_vicinity:
                        area += hashmap[entry] 
                    max_cells = max(max_cells,area+1)           
        return max_cells

