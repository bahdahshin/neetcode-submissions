class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                s = (r // 3, c // 3)
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in cols[c]:
                    return False
                if board[r][c] in squares[s]:
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[s].add(board[r][c])
                
        return True