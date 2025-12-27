'''
Problem name: Evaluate Reverse Polish Notation

Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

Description: 
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.


My Thought Process:
The idea was to first store the operators through a hash map to avoid repetitive if checks. Then
use a stack to keep track of numbers. I used a for each loop to track the input then just keep
appending to the stack until we find an operation where we simply just get the top 2 elements
and perform the operation on them, where the top of the stack is the first number in the operation. 
We then store the result and append it to the top of the stack. At the end of the loop, just return
the result which is the final element left on the stack.

Time & space complexity:
O(n) time
O(n) space

'''

class Solution(object):
    def evalRPN(self, tokens):
        import operator
        stack = []
        ops = {"+":operator.add, 
               "-":operator.sub, 
               "*":operator.mul, 
               "/":operator.truediv}

        for c in tokens:
            if c in ops:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                result = ops[c](num2, num1)
                stack.append(result)
            else:
                stack.append(c)
                
        return int(stack[-1])

g = Solution()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(g.evalRPN(tokens))



'''
class Solution(object):
    def evalRPN(self, tokens):
        import operator
        stack = []
        ops = {"+":operator.add, 
               "-":operator.sub, 
               "*":operator.mul, 
               "/":operator.floordiv}
        
        result = 0

        for c in tokens:
            if c in ops:
                while stack:
                    num = int(stack.pop())
                    result = ops[c](result, num)
            else:
                stack.append(c)
                
        return result
'''