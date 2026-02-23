'''
Problem name: Binary Tree Maximum Path Sum

Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

Description: 
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge 
connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass 
through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

My Thought Process:
The idea was to simply use a dfs to traverse through the tree and use a global variable compare if the current node's
sum with it's children are greater than that current value of the global variable. After that, we simply return the
child with the greater value added with the current node value.

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
    def maxPathSum(self, root):
        self.max = float('-inf')

        def dfs(cur):
            if not cur:
                return 0
            
            left = max(dfs(cur.left), 0)
            right = max(dfs(cur.right), 0)

            self.max = max(self.max, left + right + cur.val)

            return cur.val + max(left, right)
    
        dfs(root)

        return self.max

g = Solution()

root = [-15,10,20,None,None,15,5,-5]
root = list_to_tree(root)

print(g.maxPathSum(root))





