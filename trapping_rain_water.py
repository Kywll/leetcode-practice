'''
Problem name: Trapping Rain Water

Link: https://leetcode.com/problems/trapping-rain-water/

Description: 
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water 
it can trap after raining.


My Thought Process:
Whiteboard approach(intuition) - My approach was to first count the area of the first height that I will encounter, and from that point on, I then subtract any heights that is not greater than the current level
to the total area. If I found 2 heights that is greater than the current level, I set the current level into that then add up the area on top of the previous level and starts subtracting the upcoming heights
that is not greater than the current level now. I repeat this until I explored all heights.

Code process - I used a two pointer pattern for this problem and I simply moved the pointer of the lower height otherwise just move the left one if it's equal. I then subtracted the height of the pointer
that will is lower. I added an area whenever two heights was found that is greater than the current level, then set the current level to the lower one of those two.

Time & space complexity:
O(n) time
O(1) space

'''

class Solution(object):
    def trap(self, height):
        i = 0
        j = len(height)-1

        total_area = 0
        cur_level = 0
        prev_level = 0

        
        while i < j:
            if height[i] <= height[j]:
                if prev_level > 0:
                    if height[i] > cur_level:
                        total_area-=cur_level
                    else:
                        total_area -= height[i]

            elif height[i] > height[j]:
                if prev_level > 0:
                    if height[j] > cur_level:
                        total_area-=cur_level
                    else:
                        total_area -= height[j]

            lower = height[i] if height[i] < height[j] else height[j]
            elements_between = (j-i)-1
            if lower > cur_level:
                total_area += elements_between * (lower-cur_level)
                cur_level = lower

            if height[i] <= height[j]:
                i+=1

            elif height[i] > height[j]:
                j-=1

            prev_level = cur_level
            print(total_area)
        return total_area
    
#What I have to figure out
#Do not reduce the first addition(the outermost heights)
#Do reduce the current index but only once


g = Solution()
height = [2,1,0,2]
print(g.trap(height))


'''
Revised Version:

Just mixed the subtraction with the left and right pointer movement conditions 


'''

class Solution(object):
    def trap(self, height):
        i = 0
        j = len(height)-1

        total_area = 0
        cur_level = 0
        prev_level = 0

        while i < j:
            lower = height[i] if height[i] < height[j] else height[j]
            elements_between = (j-i)-1
            if lower > cur_level:
                total_area += elements_between * (lower-cur_level)
                cur_level = lower

            if height[i] <= height[j]:
                if prev_level > 0:
                    if height[i] > prev_level:
                        total_area-=prev_level
                    else:
                        total_area -= height[i]
                i+=1

            elif height[i] > height[j]:
                if prev_level > 0:
                    if height[j] > prev_level:
                        total_area-=prev_level
                    else:
                        total_area -= height[j]
                j-=1
                
            prev_level = cur_level
            
        return total_area
    
    
g = Solution()
height = [2,1,0,2]
print(g.trap(height))