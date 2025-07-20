class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        start, end = 0, rows * cols - 1
        while start <= end:
            mid = (start + end) // 2
            row, col = divmod(mid, cols)
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
