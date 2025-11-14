'''
Title: How Many Numbers Are Smaller Than the Current Number

Link: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/?envType=problem-list-v2&envId=sorting

Description:
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than 
it. That is, for each nums[i] you have to count the number of valid j's such that j != i and 
nums[j] < nums[i].

My Thought Process:
The bruteforce idea is to simple iterate through the array with 2 loops and keep comparing 
and store the values in count then place it on result array.

Time & space complexity:
O(n^2) time
O(1) space

'''



class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result = []
        
        for i in range(len(nums)):
            count = 0
            j = 0
            while j < len(nums):
                if nums[i] > nums[j] and j != i:
                    count+=1
                j+=1
            result.append(count)
        return result

g = Solution()

nums = [7,7,7,7]

print(g.smallerNumbersThanCurrent(nums))








