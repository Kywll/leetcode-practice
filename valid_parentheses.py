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
The ideas is to use a stack so that you could know easily when you see a closing bracket and could
easily check if it is closed properly. The checking is done by using a hashmap where the closing
bracket is the key and the opening is the value. This is done so that if you found a closing bracket
you could check on the stack if it is the opening bracket of the closing bracket you found otherwise,
that means that it is not valid. If you found an opening bracket, just append it to the stack.

Time & space complexity:
O(n) time
O(n) space

What I learned:
I learned that you could use stacks to store items from another list and use it to check if the next
few elements contains what you want from the previous ones. This is specially useful when order 
matters and matching pairs where you need to compare current elements with previously seen ones.
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
