'''
Problem name: Search in Rotated Sorted Array

Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/

Description: 
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

My thought process:
The idea is to first find the pivot then check which side the target is, you can do this by checking
if target is less than or equals the last element, which means it's on the right side, if not, then 
it's on the left side.

Time & space complexity:
O(logn) time
O(1) space

'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid+1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -=1

        pivot = left
    
        if target <= nums[len(nums)-1]:
            right = len(nums)-1
            left = pivot
        else:
            right = pivot-1
            left = 0

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid +1
            else:
                right = mid -1

        return -1


g = Solution()

nums = [4,5,6,7,0,1,2]
target = 5

print(g.search(nums, target))





