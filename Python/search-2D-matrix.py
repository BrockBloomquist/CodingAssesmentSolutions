class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        Time Complexity O(log(n*m)), Space Complexity O(1)
        """
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])

        start, end = 0, (rows * cols) - 1

        while start <= end:
            mid = (start + end) // 2
            value = matrix[mid // cols][mid % cols]
            if value == target:
                return True
            elif value < target:
                start = mid + 1
            else:
                end = mid - 1
        return False