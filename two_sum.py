'''
Title: Two Sum

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

My Thought Process:
Since the problem is looking to get the sum of a number by adding two indices but also requires
you to not add the same indicies, you can simply use a nested for loop that iterates through
the list. i = 0 so that it starts at the first index, and j = 1 so that it starts at the 2nd
index and i should loop until nums-1 so that it won't reach the last index which would
prevent the same indices adding together


Time & space complexity:
O(n^2) time complexity
O(n) time complexity

'''
class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    result.append(i)
                    result.append(j)
                    return result
                j+=1
            i+=1

nums = [2,7,11,15]
target = 9

g = Solution()
print(g.twoSum(nums, target))




class Better_Solution(object):
    def twoSum(self, nums, target):
        result = []
        

nums = [1, 2, 3, 4, 5]
target = 9

k = Better_Solution()

print(k.twoSum(nums, target))

'''
Challenge:
Can you come up with an algorithm that is less than O(n^2) time complexity?


Time & space complexity:


'''