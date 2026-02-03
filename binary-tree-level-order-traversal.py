'''
Problem name: Lowest Common Ancestor in Binary Search Tree

Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Description: 
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level 
by level).

My Thought Process:
The idea was to use a bfs and store them in a result level by level. We do this by using a nested for loop that iterates
through the previous length of the queue so that we could update the queue without visiting the new ones yet which allows
use to store levels.

Time & space complexity:s
O(n) time
O(n) space

What I Learned:
I learned that when using bfs on trees, I could find the level of the nodes by using a nested for loop that iterates
on the length of the queue and popping the nodes from there then appending the childs back to the queue so that it still
updates the queue but you only iterate through the current level and not immediately going through the new ones and 
allow you to store those values.
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(arr):
    
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        node = q.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            q.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            q.append(node.right)
        i += 1

    return root


def print_level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

class Solution:
    def levelOrder(self, root):        
        result = []
        queue = deque([root])

        while queue:
            qLen = len(queue)
            level = []
            for i in range(qLen):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)

                    queue.append(curr.left)
                    queue.append(curr.right)
            if level:    
                result.append(level)

        return result
 
g = Solution()

root = [3,9,20,None,None,15,7]
root = list_to_tree(root)


print(g.levelOrder(root))





