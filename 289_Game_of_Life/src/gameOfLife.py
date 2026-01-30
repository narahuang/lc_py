class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [
            (-1, 1), (0, 1), (1, 1), (-1, 0),
            (1, 0), (-1, -1), (0, -1), (1, -1)
        ]
        # Count living neighbors
        rows = len(board)
        columns = len(board[0])
        for row in range(rows):
            for col in range(columns):
                count = 0
                for direction in directions:
                    chk_pos = (row + direction[0], col + direction[1])
                    # Check position boundaries
                    if (
                        chk_pos[0] < 0
                        or chk_pos[0] >= rows
                        or chk_pos[1] < 0
                        or chk_pos[1] >= columns
                    ):
                        continue
                    # Check last bit for current neighbor status
                    if board[chk_pos[0]][chk_pos[1]] % 2 == 1:
                        count += 1
                # Assigning new status to second-last bit
                if board[row][col] == 1 and (count < 2 or count > 3):
                    board[row][col] = 1
                elif board[row][col] == 0 and count == 3:
                    board[row][col] = 2
                elif board[row][col] == 1 and (2 <= count <= 3):
                    board[row][col] = 3
        # Shift all bits to the right to get final result
        for row in range(rows):
            for col in range(columns):
                board[row][col] = board[row][col] >> 1
        return board
