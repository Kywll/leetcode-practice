'''
Problem name: Count Good Nodes in Binary Tree

Link: https://leetcode.com/problems/binary-tree-right-side-view/description/

Description: 
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

My Thought Process:
The idea was to use preorder traversal and pass a most value through the dfs and check if the value of the current node
is greater or equals than the seen most so far, if yes, you simply just add 1 to the result and pass the value of that
into the child, so it becomes the current most. If the current node is lesser than the most, then you simply skip it and
go to the children.

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
    def goodNodes(self, root):        
        self.result = 0
        
        def dfs(node, most):
            if not node:
                return
            
            if node.val >= most:
                self.result += 1
                most = node.val

            left = dfs(node.left, most)
            right = dfs(node.right, most)

            return node

        dfs(root, root.val)

        return self.result
 
g = Solution()

root = [3,1,4,3,None,1,5]
root = list_to_tree(root)


print(g.goodNodes(root))





