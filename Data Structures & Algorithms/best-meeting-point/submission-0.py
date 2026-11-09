class Solution:
    def manhattanDistance(self,point1,point2):
        rows_distance = abs(point1[0]-point2[0])
        cols_distance = abs(point1[1]-point2[1])
        return rows_distance+cols_distance
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        row_f = []
        row_c = []
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    row_f.append(i)
                    row_c.append(j)
        row_f.sort()
        row_c.sort()
        median_r = row_f[len(row_f)//2]
        median_c = row_c[len(row_c)//2]
        row_distance = [abs(i-median_r) for i in row_f]
        col_distance = [abs(i-median_c) for i in row_c]
        return sum(row_distance)+sum(col_distance)

               

