class Solution:
    def dfs(
        self, board: List[List[str]], word: str, index: int, i: int, j: int, visited: set
    ) -> bool:
        if index == len(word) - 1:
            return True
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right,left,down, up
        visited.add((i, j))  # add it to the list of coords we've already visited
        result = False
        for x, y in directions:
            delta_x = i + x
            delta_y = j + y
            if (
                (delta_x >= 0) and (delta_x < ROWS) and (delta_y >= 0) and (delta_y < COLS)
            ):  # valid combinations only
                if (delta_x, delta_y) not in visited:
                    if board[delta_x][delta_y] == word[index + 1]:  # next letter match
                        result = result or self.dfs(
                            board, word, index + 1, delta_x, delta_y, visited
                        )
                        if result:
                            return True
        visited.remove((i, j))
        return result

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        ROWS = len(board)
        COLS = len(board[0])
        result = False

        for i in range(ROWS):
            for j in range(COLS):
                if word[0] == board[i][j]:  # first letter matches
                    visited = set()
                    result = result or self.dfs(board, word, 0, i, j, visited)
        return result
