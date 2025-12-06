'''
Problem name: Find the Number of Good Pairs I

Link: https://leetcode.com/problems/find-the-number-of-good-pairs-i/?envType=problem-list-v2&envId=hash-table

Description: 
You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.


My thought process:

Time & space complexity:


'''


class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        count = 0
        for i in nums1:
            for j in nums2:
                if i % (j*k) == 0:
                    count += 1
        return count
        