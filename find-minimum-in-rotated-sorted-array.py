'''
Problem name: Find Minimum in Rotated Sorted Array

Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Description: 
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

My thought process:
The idea is to get the middle first and check if it's greater than the right pointer, if it does, then 
that means we are on the left side group of the rotated sorted array which we could then just set the
left pointer into the middle. If it's less than the right then that means we are on the lower side 
of the array which means we can just put the right pointer into the mid. If equals, then just move 
right once.

Time & space complexity:
O(log n) time
O(1) space
'''

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right-=1

        return nums[left]

        


        


g = Solution()

nums = [3,4,5,1,2]

print(g.findMin(nums))