'''
Problem name: Lowest Common Ancestor in Binary Search Tree

Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/

Description: 
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the 
lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

My Thought Process:
The idea is that each node that is lower than the current node is guranteed to be on the left side and vice versa. That
means we could take advantage of the fact that we could simply check if both p and q are less than or greater than the 
current node, if it is, just go to that direction. If they are not the same then that means that the current node is the
LCA because both the p and q is split up and the only way for them to meet is through the current node.

Time & space complexity:
O(log n) time
O(1) space

What I learned:
You could use an iterative approach for BST and you could just keep comparing if a node you have is greater or equals to
the current node which means that you will know if it's somewhere on the left or right side.
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
    def lowestCommonAncestor(self, root, p, q):
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
 
g = Solution()

root = [5,3,8,1,4,7,9,None,2]
root = list_to_tree(root)

p = list_to_tree([2]) 
q = list_to_tree([8])

print(g.lowestCommonAncestor(root, p, q).val)





