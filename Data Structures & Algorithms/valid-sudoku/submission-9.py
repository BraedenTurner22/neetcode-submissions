class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        columnMap = defaultdict(set)
        squareMap = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    if board[r][c] in rowMap[r]:
                        return False
                    if board[r][c] in columnMap[c]:
                        return False
                    if board[r][c] in squareMap[(r//3, c//3)]:
                        return False
                    rowMap[r].add(board[r][c])
                    columnMap[c].add(board[r][c])
                    squareMap[(r//3, c//3)].add(board[r][c])
        
        return True