class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        friends  = []
        ROWS = len(grid)
        COLS = len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    friends.append((i,j))
        median_index = len(friends)//2
        rows = [i[0] for i in friends]
        cols = [i[1] for i in friends]
        rows.sort()
        cols.sort()
        median_rows = rows[median_index]
        median_cols = cols[median_index]
        rows_d = [abs(i-median_rows) for i in rows]
        cols_d = [abs(i-median_cols) for i in cols]
        return sum(rows_d)+sum(cols_d)

        