'''
Problem name: Concatenation of Array

Link: https://leetcode.com/problems/concatenation-of-array/description/?envType=problem-list-v2&envId=array

Description: 
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

My thought process:
Just return nums + nums

Time & space complexity:
O(1) space and time
'''

class Solution(object):
    def getConcatenation(self, nums):
        ans = nums + nums
        return ans
g = Solution()

nums = [1,2,1]

print(g.getConcatenation(nums))




