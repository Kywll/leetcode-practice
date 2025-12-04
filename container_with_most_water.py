'''
Problem name: Container With Most Water

Link: https://leetcode.com/problems/container-with-most-water/description/

Description: 
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

My thought process:
I simply used a two pointer solution where I first checked the width of the area by subracting the 
right pointer to the left pointer, then I multiplied it to the lower one between the two heights.
I compared the sums and returned the highest one.

Time & space complexity:
O(n) time
O(1) space

'''

class Solution(object):
    def maxArea(self, height):
        top = 0

        i = 0
        j = len(height)-1
        while i < j:
            width = (j - i)
            final_height = height[i] if height[i] < height[j] else height[j] 
            if width * final_height > top:
                top = width * final_height
            if height[i] > height[j]:
                j-=1
            elif height[i] <= height[j]:
                i+=1
        return top


g = Solution()

height = [1,8,6,2,5,4,8,3,7]

print(g.maxArea(height))







