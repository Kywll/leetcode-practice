'''
Problem name: Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=array
Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

My thought process:
The approach I did was to start at the end of the array in order to compare whether the index 
of first array and second array was greater, and if it is, then you simply set the value at
the end to the value of the index of 2nd array. I basically used 2 pointers where i is equals 
to the end of the 1st array(the ones with actual numbers) and j is equals to the end of 2nd 
array, I also have k which is equals to the very end of the first array(the zeroes) which tracks
where you can place the current highest value between the current index of both arrays. 
In case that the second array has more array, I made another loop at the end so that the lefover
elements in the second array will be automatically placed in nums1[k].


Time & space complexity:
O(n + m) time
O(1) space

What I learned:
You can sometimes simplify pointer problems by starting from the end of the array, especially 
when merging in-place. This approach prevents overwriting elements that haven't been compared 
yet and often leads to cleaner, more efficient solutions.
'''

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m-1
        j = n-1
        k = (m+n)-1

        while k >= 0 and i >= 0 and j >= 0:
            print("first", i, j, nums1)
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            elif nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j-=1
            print("second", i, j, nums1)
            
            k-=1

        while j >= 0 and k >= 0:
            nums1[k] = nums2[j]
            k-=1
            j-=1

        return nums1


nums1 = [0]
m = 0
nums2 = [1]
n = 1

g = Solution()

print(g.merge(nums1, m, nums2, n))









