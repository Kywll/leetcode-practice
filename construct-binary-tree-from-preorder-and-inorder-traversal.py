'''
Problem name: Construct Binary Tree from Preorder and Inorder Traversal

Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

Description: 
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and 
inorder is the inorder traversal of the same tree, construct and return the binary tree.

My Thought Process:
The idea was that the preoder's first index is always going to be the head and if you find the index of the head in the
inorder list, everything to it's left is the left nodes, and everything to the right is the right nodes. So based on
that, what we could do is slice them based on the value of the index of the head in the inorder list and pass it to 
recursion for the left and right values of the current node. That way, we would be able to construct the tree based on 
those informations.

Time & space complexity:
O(n^2) time
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
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        inorder_map = {}
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx
        
        root = TreeNode(preorder[0])
        mid = inorder_map[preorder[0]]

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root
 
g = Solution()

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

print_level_order(g.buildTree(preorder, inorder))





