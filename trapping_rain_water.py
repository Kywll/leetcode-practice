'''
Problem name: Trapping Rain Water

Link: https://leetcode.com/problems/trapping-rain-water/

Description: 
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water 
it can trap after raining.


My Thought Process:


Time & space complexity:


'''

class Solution(object):
    def trap(self, height):
        total_area = 0
        i = 0
        j = len(height)-1

        prev_level = 0
        cur_level = 0

        highest_left = 0
        highest_right = 0
        
        while i < j:
            if height[i] <= height[j]:
                pass


height = [0,1,0,2,1,0,1,3,2,1,2,1]




