'''
Problem name: Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=array
Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

My thought process:



Time & space complexity:

'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        result = nums1[:m-1]
        
        i = m-1
        j = n-1
        while i >= 0 and j >=0:
            if result[i] < nums2[j]:
                nums1[i+j] = nums2[j]
                j-=1
            elif result[i] > nums2[j]:
                nums1[i+j] = nums1[Z]
                j-=1
            


nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6]
n = 3

g = Solution()

print(g.merge(nums1, m, nums2, n))









