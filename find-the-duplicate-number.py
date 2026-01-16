'''
Problem name: Find the Duplicate Number

Link: https://leetcode.com/problems/find-the-duplicate-number/description/

Description: 
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

My thought process:
The idea was to just use a set to check if there is a duplicate.

Time & space complexity:
O(n) time
O(n) space

'''

class Solution:
    def findDuplicate(self, nums):
        empty_set = set()

        for num in nums:
            if num in empty_set:
                return num
            else:
                empty_set.add(num)

g = Solution()

nums = [1,3,4,2,2]

print(g.findDuplicate(nums))


