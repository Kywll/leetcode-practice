'''
Problem name: Build Array from Permutation

Link: https://leetcode.com/problems/build-array-from-permutation/description/?envType=problem-list-v2&envId=array

Description: 

My thought process:
Just loop through the array and store the vallue of nums[nums[i]] into result

Time & space complexity:
O(n) time
O(1) space

'''


class Solution(object):
    def buildArray(self, nums):
        result = []
        for i in range(len(nums)):
            result.append(nums[nums[i]])
        return result

nums = [0,2,1,5,3,4]

g = Solution()

print(g.buildArray(nums))
