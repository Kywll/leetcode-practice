'''
Problem name: Remove Element
Link: https://leetcode.com/problems/remove-element/description/?envType=problem-list-v2&envId=array
Description: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

My thought process:
Since we are simply trying to remove the numbers that is equals to val, we can simply have 2 
2 pointers both starting at 0 and check if the right pointer is not equals to the target, and if
it is, then we make the value of the left pointer into the right pointer since we want the number
not equals to target to be included then we increment the left index as well as the right index.
If the right index is equals to the target, we simply ignore it and increment the right index.

Time & space complexity:
O(n) time
O(1) space


'''



class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        j = 0
        while j < len(nums) and i < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i+=1
            j+=1
        return i


g = Solution()

nums = [3,2,2,3]
val = 3

print(g.removeElement(nums, val))



'''
Thought Process and What I learned:
Since the right pointer will interate through the entire array, you know exactly how many steps
it will take which is less then the length of the array, that means you can use a for loop for
it. This works even with 2 pointers because the left pointer(i) is not determined and will most
likely be shorter than the right pointer on average due to it being dependent on it. You don't
have to make 2 loops as well. 
'''

class BetterSolution(object):
    def removeElement(self, nums, val):
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
