'''
Problem name: Transform Array by Parity

Link: https://leetcode.com/problems/transform-array-by-parity/description/?envType=problem-list-v2&envId=sorting
Description: 
You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:

Replace each even number with 0.
Replace each odd numbers with 1.
Sort the modified array in non-decreasing order.
Return the resulting array after performing these operations.


My thought process:
We simply have to loop through the array and check if the current index modulux to 2 is equals 
to zero which means it's an even number where we simply make it equals to 0 otherwise, just
turn the value of current index into 1.

Time & space complexity:
O(n) time
O(1) space
'''

class Solution(object):
    def transformArray(self, nums):
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1

        nums = sorted(nums)
        return nums

g = Solution()

nums = [1,5,1,4,2]

print(g.transformArray(nums))


