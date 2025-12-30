'''
Problem name: Binary Search

Link: https://neetcode.io/problems/binary-search/question?list=neetcode150

Description: 
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time


My thought process:
This is a classic binary search alogrithm where we simply just get the middle every time until
we find the target based on if the middle is lower or greater than the target.

Time & space complexity:
O(logn) time
o(1) space

'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1

        return -1

g = Solution()

nums = [-1,0,2,4,6,8]
target = 4

print(g.search(nums, target))
