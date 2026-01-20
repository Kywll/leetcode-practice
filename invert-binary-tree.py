'''
Title: Invert Binary Tree

Link: https://leetcode.com/problems/invert-binary-tree/description/

Description:
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than 
it. That is, for each nums[i] you have to count the number of valid j's such that j != i and 
nums[j] < nums[i].

My Thought Process:
Used a post order apprach where I just switched out the left and right nodes of the trees.

Time & space complexity:
O(n) time
O(1) space

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
    def invertTree(self, root):
        if root is None:
            return
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        temp = root.left
        root.left = root.right
        root.right = temp

        return root

g = Solution()

root = [4,2,7,1,3,6,9]
root = list_to_tree(root)
print_level_order(g.invertTree(root))

