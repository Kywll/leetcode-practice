'''
Problem name: Valid Parentheses

Link: https://leetcode.com/problems/valid-parentheses/description/

Description: 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

My thought process:

Time & space complexity:


'''



class Solution(object):
    def isValid(self, s):
        stack = []
        dic = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in dic:
                if len(stack) == 0:
                    return False
                
                elif stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if len(stack) == 0:
            return True
        
        return False


s = "()[}"

g = Solution()
print(g.isValid(s))
