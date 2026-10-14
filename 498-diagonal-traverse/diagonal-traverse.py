class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        M , N = len(mat) , len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1

        while len(result) < M * N:
            result.append(mat[row][col])
            
            if direction == 1:
                if col == N - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:
                if row == M - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1
        return result