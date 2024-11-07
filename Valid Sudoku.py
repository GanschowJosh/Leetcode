def isValidSudoku(board: list[list[str]]) -> bool:
    def is_valid(unit):
        unit = [num for num in unit if num != "."]
        return len(unit) == len(set(unit))

    for row in board:
        if not is_valid(row):
            return False

    for col in zip(*board):
        if not is_valid(col):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid(subgrid):
                return False

    return True

        