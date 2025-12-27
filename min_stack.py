'''
Problem name: Min Stack

Link: https://leetcode.com/problems/min-stack/description/

Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.


My thought process:
The idea was to use another stack to keep storing the current value inside the stack.

Time & space complexity:
O(1) time
O(n) space

What I learned:
I learned that I could use another stack to keep track of something in your original stack.

'''

class MinStack(object):
    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val):
        self.stack.append(val)

        if self.minStack:
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

        return False

    def top(self):
        print(self.stack[-1])
        return self.stack[-1]
        
    def getMin(self):
        print(self.minStack[-1])
        return self.minStack[-1]



minStack = MinStack()


minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()
minStack.pop()
minStack.top()
minStack.getMin()
