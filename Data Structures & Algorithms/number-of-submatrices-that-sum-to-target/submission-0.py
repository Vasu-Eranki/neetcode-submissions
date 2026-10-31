class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        result = 0 
        if not matrix:
            return result
        ROWS = len(matrix)
        COLS = len(matrix[0])
        for row in range(ROWS):
            column = [0]*COLS
            for size_of_submatrix in range(row,ROWS):
                cumsum = 0 
                hashmap = {0:1}
                for col in range(COLS):

                    column[col]+=matrix[size_of_submatrix][col]
                    cumsum+=column[col]
                    result+=hashmap.get(cumsum-target,0)
                    hashmap[cumsum] = hashmap.get(cumsum,0)+1

        return result
