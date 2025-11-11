'''
Title: Single Number

Link: https://leetcode.com/problems/single-number/description/
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

My Thought Process:
Since I'm only looking for an element that has no duplicate, I can just store the frequencies of the keys into a hashmap and return which one
has only 1 occurence.

Time & space complexity:

'''


class Solution(object):
    def singleNumber(self, nums):
        dic = {}
        for e in nums:
            if e not in dic:
                dic[e] = 0
            dic[e] +=1
        keys = list(dic.keys())
        for key in keys:
            if dic[key] == 1:
                return key

g = Solution()

nums = [2,2,1]

print(g.singleNumber(nums))


