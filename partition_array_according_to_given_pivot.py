'''
Problem name: Partition Array According to Given Pivot
Link: https://leetcode.com/problems/partition-array-according-to-given-pivot/description/?envType=problem-list-v2&envId=array

Description:
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
Return nums after the rearrangement.

My thought process:
Just simply loop through the array and check if they are less than, equal, or greater than pivot and store them in their respective arrays(left, mid, right)
then just return the combination of the 3 arrays at the end

Time & space complexity:
O(n) time and space

'''


class Solution(object):
    def pivotArray(self, nums, pivot):
        left = []
        mid = []
        right = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] == pivot:
                mid.append(nums[i])
            elif nums[i] > pivot:
                right.append(nums[i])
        result = left + mid + right

        return result

        
g = Solution()

nums = [-3,4,3,2]
pivot = 2


print(g.pivotArray(nums, pivot))

