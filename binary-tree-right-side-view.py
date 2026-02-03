'''
Problem name: Binary Tree Right Side View

Link: https://leetcode.com/problems/binary-tree-right-side-view/description/

Description: 
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you 
can see ordered from top to bottom.

My Thought Process:
The idea was to use a level order traversal and then store the last node of each levels. This works because order level
traversal is left to right that means that the last one will always be the right side view.

Time & space complexity:s
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
    def rightSideView(self, root):        
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
                result.append(level[-1])

        return result
 
g = Solution()

root = [1,2,3,4,None,None,None,5]
root = list_to_tree(root)


print(g.rightSideView(root))





