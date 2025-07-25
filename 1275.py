class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[' ' for _ in range(3)] for _ in range(3)]

        for i, (row, col) in enumerate(moves):
            player = 'A' if i % 2 == 0 else 'B'
            mark = 'X' if player == 'A' else 'O'
            grid[row][col] = mark

            # Check if the current player won
            # Check rows
            if grid[row][0] == grid[row][1] == grid[row][2] == mark:
                return player
            # Check columns
            if grid[0][col] == grid[1][col] == grid[2][col] == mark:
                return player
            # Check diagonals
            if (row == col) and (grid[0][0] == grid[1][1] == grid[2][2] == mark):
                return player
                # check anti-diagnol
            if (row + col == 2) and (grid[0][2] == grid[1][1] == grid[2][0] == mark):
                return player

        return "Draw" if len(moves) == 9 else "Pending"