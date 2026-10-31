class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        result = 0 
        ROWS = len(matrix)
        COLS = len(matrix[0])
        for row in range(ROWS):
            column = [0]*COLS
            for bottom in range(row,ROWS):
                cumsum = 0 
                hashmap = {0:1}
                for col in range(COLS):
                    column[col]+=matrix[bottom][col]
                    cumsum+=column[col]
                    result+=hashmap.get(cumsum-target,0)
                    hashmap[cumsum] = hashmap.get(cumsum,0)+1
        return result
