'''
Title: Sliding Window Maximum

Link: https://leetcode.com/problems/sliding-window-maximum/description/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

My Thought Process:


Time & space complexity:


'''

import heapq

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        max_heap = []
        result = []

        l = 0

        for r in range(len(nums)):
            heapq.heappush(max_heap, (-nums[r], r))
            if (r-l+1) > k:
                l+=1
            
            
            while max_heap[0][1] < l:
                heapq.heappop(max_heap)

            if (r-l+1) == k:
                result.append(-max_heap[0][0])
                
        return result 

g = Solution()


nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(g.maxSlidingWindow(nums, k))