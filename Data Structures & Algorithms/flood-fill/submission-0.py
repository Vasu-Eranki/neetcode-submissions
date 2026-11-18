class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if not image:
            return image
        ROWS = len(image)
        COLS = len(image[0])
        visited = set()
        source_color = image[sr][sc]
        def dfs(i,j,source,visited,color):
            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            visited.add((i,j))
            image[i][j]=color
            for x,y in directions:
                delta_x = x+i
                delta_y = j+y
                if (delta_x>=0 and delta_x<ROWS and delta_y>=0 and delta_y<COLS):
                    if image[delta_x][delta_y]==source:
                        if ((delta_x,delta_y) not in visited):
                            dfs(delta_x,delta_y,source,visited,color)
        dfs(sr,sc,source_color,visited,color)
        return image


        