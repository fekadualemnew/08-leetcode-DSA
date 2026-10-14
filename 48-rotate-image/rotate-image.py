class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])

        for r in range(M):
            for c in range(r, N):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for r in range(M):
            matrix[r].reverse()

        return matrix
        