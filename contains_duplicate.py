'''
Problem name: Contains Duplicate

Link: https://leetcode.com/problems/contains-duplicate/description/


Description: 
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
My thought process:

My Thought Process:
The first bruteforce intuition is to simply use a nested loop to check if an index is equals to
other indices but that will cose O(n^2) so I simply used a hashmap where I check each time if
the current index is in the hashmap which I would then return True. But if not, then I simply
return False after the loop.

Time & space complexity:
O(n)
O(n)

'''

class Solution(object):
    def containsDuplicate(self, nums):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic[nums[i]] = i
        return False

g = Solution()

nums = [1,2,3,1]
print(g.containsDuplicate(nums))









