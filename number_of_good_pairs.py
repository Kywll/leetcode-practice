'''
Problem name: Number of Good Pairs
Link: https://leetcode.com/problems/number-of-good-pairs/description/?envType=problem-list-v2&envId=array

Description:
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

My thought process:
Just simply loop through the array and have a nested loop inside that starts with the value of
the outside loop. 

Time & space complexity:
O(n^2) time
O(1) space

'''


class Solution(object):
    def numIdenticalPairs(self, nums):
        result = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    result += 1
        return result

g = Solution()

nums = [1,1,1,1]

print(g.numIdenticalPairs(nums))






