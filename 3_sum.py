'''
Problem name: 3Sum

Link: https://leetcode.com/problems/3sum/description/

Description: 
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

My thought process:
I simply sorted the array and used a two pointer approach. I used a nested loop to do so. The idea was to to keep and index to the loop and use a two pointer on the right. This is
possible due to it being sorted where I could simply check if the sum of the two pointers is greater or less than the inverse of the current index which I then simply move the left
or right pointer once until I found an answer which I then move both pointers. This is done until the left pointer is no longer less than the right pointer.

Time & space complexity:
O(n^3) time due to checking if combination is already in result
O(1) space
'''


class Solution(object):
    def threeSum(self, nums):
        result = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                if sorted_nums[j] + sorted_nums[k] == sorted_nums[i] *-1:
                    if [sorted_nums[i], sorted_nums[j], sorted_nums[k]] not in result:
                        result.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    j+=1
                    k-=1
                elif sorted_nums[j] + sorted_nums[k] < sorted_nums[i] *-1:
                    j+=1
                elif sorted_nums[j] + sorted_nums[k] > sorted_nums[i] *-1:
                    k-=1
        return result



g = Solution()

nums = [-2,0,1,1,2]

print(g.threeSum(nums))



