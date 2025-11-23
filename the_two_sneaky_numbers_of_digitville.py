'''
Problem name: The Two Sneaky Numbers of Digitville

Link: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/?envType=problem-list-v2&envId=array

Description: 
In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order), so peace can return to Digitville.

My thought process:
Just store each element in a hashmap and check if an index is a duplicate
if you found 2 duplicates, just return the result

Time & space complexity:
O(n) time and space
'''


class Solution(object):
    def getSneakyNumbers(self, nums):
        result = []
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                result.append(nums[i])
                if len(result) == 2:
                    return result
            else:
                dic[nums[i]] = i

g = Solution()

nums = [0, 1, 1, 0]

print(g.getSneakyNumbers(nums))



