'''
Problem name: Count Pairs Whose Sum is Less than Target

Link: https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/?envType=problem-list-v2&envId=array

Description: 
Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
 
My thought process:
The bruteforce solution is to simply just iterate through the array with nest loops with the inner 
starting at i+1.

Time & space complexity:
O(n^2) time
O(1) time

'''

class Solution(object):
    def countPairs(self, nums, target):
        result = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                print(nums[i], nums[j])
                if nums[i] + nums[j] < target:
                    result +=1
        return result

g = Solution()

nums = [-1,1,2,3,1]
target = 2
print(g.countPairs(nums, target))


