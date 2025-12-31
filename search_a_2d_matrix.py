'''
Problem name: Search a 2D Matrix

Link: https://leetcode.com/problems/search-a-2d-matrix/description/

Description: 
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

My thought process:
My idea was to simple loop through each row then just use binary search on the columns of each row. 
However, this is an inefficient solution.

Time & space complexity:
O(nlogm) time
O(1) space

'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i])-1
            while left <= right:
                mid = [i, (left + right) // 2]
                if matrix[mid[0]][mid[1]] == target:
                    return True
                elif matrix[mid[0]][mid[1]] < target:
                    left = mid[1]+1
                elif matrix[mid[0]][mid[1]] > target:
                    right = mid[1]-1
            
        return False
        

g = Solution()

matrix = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]
target = 13

print(g.searchMatrix(matrix, target))


'''
Optimal Solution:

O(log(n * m)) time
O(1) space


Explanation:
The idea was to do a binary search on the corners of the rows and check if the target is within the
range of the row, if not, you just check if it's less than the first row which means that it is 
on the earlier column and vice versa. After that, you just do binary search on the columns of the
chosen row.

'''

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left_row = 0
        right_row = len(matrix)-1
        mid_row = (left_row + right_row) // 2
        

        while left_row <= right_row:
            mid_row = (left_row + right_row) // 2
            if matrix[mid_row][0] <= target and matrix[mid_row][-1] >= target:
                break
            elif matrix[mid_row][-1] > target:
                right_row = mid_row -1
            elif matrix[mid_row][0] < target:
                left_row = mid_row +1

        left = 0
        right = len(matrix[mid_row])-1

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid_row][mid] == target:
                return True
            if matrix[mid_row][mid] < target:
                left = mid + 1
            if matrix[mid_row][mid] > target:
                right = mid - 1
            
        return False
        

g = Solution()

matrix = [[1,3,5,7], [10,11,16,20], [23,30,34,60]]
target = 13

print(g.searchMatrix(matrix, target))


