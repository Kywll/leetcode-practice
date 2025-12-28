'''
Problem name: Daily Temperatures

Link: https://leetcode.com/problems/daily-temperatures/description/

Description: 
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

My thought process:
The thought process behind the solution was to use a stack to store indices and check if the current
iteration is greater than the last index element at the stack which is only kept if there is no
greater element than them so that means they are in a non increasing order and are called monotonic 
decreasing stack. After finding an element that is greater than the top of the stack, you just store
the difference of current index to the index of top of the stack into the answer array which is 
pre-initialized list consisting of 0 values which is the default whenever there is no greater 
element next to an element. After that you just append the current index to the stack. Then return
the answer after the loop.


Time & space complexity:
O(n) time
O(n) space

What I learned:
I learned about monotonic decreasing stack and a way that it can be used to solve problems that 
requires you to previous elements to the current one. Basically just trying to find the next or
previous great element.

'''

class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return answer

g = Solution()

temperatures = [73,74,75,71,69,72,76,73]

print(g.dailyTemperatures(temperatures))
