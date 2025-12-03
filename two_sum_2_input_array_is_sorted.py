'''
Problem name: Two Sum II - Input Array Is Sorted

Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Description: 
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

My Thought Process:
I simply used a two pointer solution and I checked if the sum of the
pointers are equals to the target, otherwise if it's higher, then I 
move the right pointer once, if it's lower than target then I move
the left pointer once. I returned [i+1, j+1] since it requires 1-index

Time & space complexity:
o(n) time
O(1) space


'''


class Solution(object):
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers)-1
        while i <= len(numbers)-1 and j >= 0:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] > target:
                j-=1
            else:
                i+=1
                
        return [-1, -1]
    
g = Solution()

numbers = [2,7,11,15]
target = 9

numbers = [-5,-3,0,2,4,6,8]
target = 5
print(g.twoSum(numbers, target))

