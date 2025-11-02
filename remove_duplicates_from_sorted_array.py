'''
Problem name: Remove Duplicates from Sorted Array
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=problem-list-v2&envId=array
Description: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

My thought process:
The approach was to iterate through the list with two pointers which is i and j then you try to
see if their values are equal, if yes, then you remove the value of the pointer ahead which is
j. However, if it's not equals, then you just increment them both by one to move forward.


Time & space complexity:
O(n^2) time due to using pop() 
O(1) space

'''

class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            else:
                i+=1
                j+=1
        k = len(nums)
        return k


nums = [1,1,1,1,1,1]
g = Solution()

print(g.removeDuplicates(nums))

class BetterSolution(object):
    def removeDuplicates(self, nums):
        i = 1
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i+=1
            j+=1
        return i

nums = [1,1, 2]
h = BetterSolution()

print(h.removeDuplicates(nums))

'''
Thought Process:
So the thought process is to have 2 pointers that scans the array and make the right pointer
scan ahead and check if the left of the right pointer is equals to it or not. If yes, then that
means it is a duplicate and you simply have to move on, if not then that means that the current
index of right pointer is unique and you have to set the value of left pointer index into the 
value of right pointer current index, this is done so that it takes 0(1) space complexity
and done in place.

What I learned:
A different way to use 2 different pointers
'''