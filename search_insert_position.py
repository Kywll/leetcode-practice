'''
Problem name: Search Insert Position

Link: https://leetcode.com/problems/search-insert-position/description/?envType=problem-list-v2&envId=array

Description: 
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

My thought process:
Since the challenge is simply looking for the target where the index is then I could simply just
use a binary search where I look at the middle first and check if the middle indes is lower or 
higher than the target. It also fits because the challenge is looking to have a O(log n) time 
which is exactly what binary search is. The condition for the loop is low<=high where low = 0
and high = the length of the array minus 1. This works because each time that mid is not equals
to target, you either add or subtract which means low would eventually be greater than high.
If the target is not found, just return low or high since that is where it would stop due to
adding and substracting of low and high.

Time & space complexity:
O(log n) time
O(n)

'''


class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if  nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
        return low

nums = [1,3,5,6] 
target = 7


g = Solution()

print(g.searchInsert(nums, target))



