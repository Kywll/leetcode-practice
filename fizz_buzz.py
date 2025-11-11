'''
Problem name: Fizz Buzz
Link: https://leetcode.com/problems/fizz-buzz/description/

Description:
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

My thought process:


Time & space complexity:

'''


class Solution(object):
    def fizzBuzz(self, n):
        result = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            elif i % 5 != 0 and i % 3 != 0:
                result.append(str(i))
        return result
    
g = Solution()


n = 3

print(g.fizzBuzz(n))






