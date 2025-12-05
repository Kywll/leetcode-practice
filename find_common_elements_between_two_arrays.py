'''
Problem name: Find Common Elements Between Two Arrays

Link: https://leetcode.com/problems/find-common-elements-between-two-arrays/description/?envType=problem-list-v2&envId=hash-table

Description: 
You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].


My thought process:


Time & space complexity:


'''


class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        
        count1 = 0
        count2 = 0
        
        for x in nums1:
            if x in s2:
                count1 += 1
                
        for x in nums2:
            if x in s1:
                count2 += 1
                
        return [count1, count2]


class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        result = []
        dic = {}
        for num in nums1:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1
        for num in nums2:
            if num in dic:
                return [num, dic[num]]
        

g = Solution()

nums1 = [2,3,2]
nums2 = [1,2]

print(g.findIntersectionValues(nums1, nums2))





