'''
Problem name: Kth Smallest Element in a BST

Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Description: 
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

My Thought Process:
The idea was to do an inorder dfs traversal and store each value in a global variable, it would also be in a sorted
result due to the nature of bst. Then just return the kth element -1 (because k is 1 indexed) of the global variable.

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
    def kthSmallest(self, root, k):
        self.sorted = []
        def dfs(node):
            if not node:
                return
            
            left = dfs(node.left)

            self.sorted.append(node.val)
            
            right = dfs(node.right)

            return node
        
        dfs(root)
        
        print(self.sorted)

        return self.sorted[k-1]
 
g = Solution()

root = [5,3,8,1,4,7,9,None,2]
root = list_to_tree(root)

k = 1

print(g.kthSmallest(root, k))





