'''
Problem name: Longest Consecutive Sequence

Link: https://leetcode.com/problems/longest-consecutive-sequence/description/

Description: 
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

My Thought Process:
I first chech if the length of the array is 0, which I then return 0. I stored the elements of nums 
into a hashmap then tracked the longest streak with a variable. I looped through the array and looped
again inside checking until there is no index + counter found in the hashmap. I then check if the 
current index is the longest sequence or not. I returned longest + 1 since the index itself is included.

Time & space complexity:
O(n^2) time
O(n) space

'''

class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        dic = {}
        for num in nums:
            dic[num] = num

        longest = 0
        i = 0
        while i <= len(nums)-1:
            counter = 1
            current_longest = 0
            while (nums[i] + counter) in dic:
                counter+=1
                current_longest +=1
            if current_longest > longest:
                longest = current_longest
            i+=1

                
        return longest + 1



g = Solution()

nums = [0, -1]

print(g.longestConsecutive(nums))





