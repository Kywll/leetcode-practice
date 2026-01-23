'''
Problem name: Balanced Binary Tree

Link: https://leetcode.com/problems/balanced-binary-tree/description/

Description: 
Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in 
height by no more than 1.

My Thought Process:
The idea is to compare the height of the children of each nodes using dfs and check if the difference is more than 1, if it
is then we know that the tree is not a balanced tree.

Time & space complexity:
O(n) time
O(n) space
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
    def isBalanced(self, root):
        self.balanced = True

        def dfs(curr):
            if curr is None:
                return 0
               
            left = dfs(curr.left)
            right = dfs(curr.right)

            if left > right + 1 or right > left + 1:
                self.balanced = False

            depth = max(left, right)

            return depth + 1
        
        dfs(root)
        
        return self.balanced



g = Solution()

root = root = [3,9,20,None,None,15,7]
root = list_to_tree(root)
print(g.isBalanced(root))




