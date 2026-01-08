'''
Problem name: Median of Two Sorted Arrays

Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/?envType=problem-list-v2&envId=string

Description: 
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

My Thought Process:
I basically just merged the array then sorted it, then I checked if the sorted array is odd where
I just get the middle, if even then I take the two middles then find the average of them.

Time & space complexity:
O(n log n) time
O(n) space

'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combine = sorted(nums1 + nums2)
        left = 0
        right = len(combine)-1

        mid = (left + right) // 2

        if len(combine) % 2 != 0:
            return combine[mid]
        
        result = (combine[mid] + combine[mid+1]) / 2
        return result                

obj = Solution()

nums1 = [1,3]
nums2 = [2]

print(obj.findMedianSortedArrays(nums1, nums2))
        


'''
Optimal Solution:
Thought Process:
The idea was that if we get a slice of the array of each arrays, we can compare the rightmost of the
slice to the adjacent values of the other and if they are both less than or equals then that means, 
we have the middle of the sorted merged array. We do this by getting the total length of them combined
and getting the half of it, then we perform a binary search on the array that has the shorter length.
Getting the middle from the binary search will serve as the end of the slice and you can just 
subtract it the the half to get the slice of the other array. We can then compare if the rightmost
of each slices is less than or equals to the adjacent of the other. If the array that we did binary
search on is greater then that means that we need to move the right pointer and search for a smaller
group, meaning that we shorten the slice and add 1 to the other array, this is again done by subracting
it to the half. If however, the other array rightmost is greater then the searched arrays adjacent, 
then that means that our searched array is too small, so we simply move the left pointer to get
a higher slice of the searched array then reduce the other array. If we did find out that both 
rightmost are not greater, then that means that we found the middle. If the total is odd, then we 
just return which one has the lower value between both adjacents because they are both adjacent 
the the slices and the slices are before the middle, since the array is sorted that means the lower 
one is the middle. If odd, that means there are 2 middle, we just do the same where we get the
lower of the adjacents but now we also have to get the higher rightmost of the slices then add
those together and divide by 2 to get the average or median. 

What I learned:
I learned that we can use binary search to get a slice or a window. I learned that we can get
the windows or slices of two sorted arrays to be able to partially sort them based on those indexes,
basically arrange their positions if they are to be sorted, this is useful if we want to find the 
median of them. I also learned about utilizing the information we have of the total length and 
use it to get more info and perform formulas using it. I also learned that we could use infinity
to handle edge cases. I learned that we could just store two values into A and B and switch them 
around based on conditions such as which is shorter so that we can gurantee that we are always 
performing operations on the array we want. 

Time Complexity:
O(log(min(n, m))) time
O(n + m) space
'''

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        left, right= 0, len(A)-1

        while True:
            i = (left + right) // 2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i +1] if (i+1 < len(A)) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j +1] if (j+1 < len(B)) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                right = i-1
            else:
                left = i +1 
                

obj = Solution()

nums1 = [1,2,3,4,5,6,7,8]
nums2 = [1,2,3,4]

print(obj.findMedianSortedArrays(nums1, nums2))
        