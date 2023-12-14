# Search a 2D Matrix

'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

         # find the row containing the target
        top, bottom = 0, ROWS - 1
        while top <= bottom:
            midR = (top + bottom) // 2
            if target > matrix[midR][-1]:
                top = midR + 1
            elif target < matrix[midR][0]:
                bottom = midR -1
            else:
                break
        
        if top > bottom:
            return False
    
         # find the column containing the target
        l, r = 0, (COLS-1)
        while l <= r:
            midC = (l + r) // 2
            if matrix[midR][midC] > target:
                r = midC - 1
            elif matrix[midR][midC] < target:
                l = midC + 1
            else:
                return True
        return False
