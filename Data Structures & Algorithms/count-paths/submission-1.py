class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(0,n):
            grid[0][i] = 1
        for i in range(0,m):
            grid[i][0] = 1
        for i in range(1,m):
            up = i-1
            for j in range(1,n):
                left = j-1 
                value = 0 
                if up>=0:
                    value+=grid[up][j]
                if left>=0:
                    value+=grid[i][left]
                grid[i][j]=value
        return grid[m-1][n-1]
        