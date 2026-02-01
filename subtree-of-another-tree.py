'''
Problem name: Subtree of Another Tree

Link: https://leetcode.com/problems/subtree-of-another-tree/description/

Description: 
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.


My Thought Process:
The idea was to just use a dfs and check every node if they are equal to a subtree, if it does then return True if not then
return False.

Time & space complexity:
O(n) time
O(n) space

What I Learned:
When doing bfs, you could use a global variable as a base case
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
    def isSubtree(self, root, subRoot):
        self.subRoot = subRoot
        self.result = False

        def bfs_compare(p, q):
            queueP = [p]
            queueQ = [q]

            i = 0
            while i < len(queueP) and i < len(queueQ):
                if queueP[i] is None and queueQ[i] is None:
                    i+=1
                    continue

                if queueP[i] is None or queueQ[i] is None:
                    return False
                
                if queueP[i].val != queueQ[i].val:
                    return False
                
                queueP.append(queueP[i].left)
                queueP.append(queueP[i].right)

                queueQ.append(queueQ[i].left)
                queueQ.append(queueQ[i].right)
                
                i+=1
            
            if i < len(queueP) or i < len(queueQ):
                return False
            
            return True
        
        def dfs(curr):
            if curr is None or self.result:
                return
               
            if bfs_compare(curr, self.subRoot):
                self.result = True
                return

            left = dfs(curr.left)
            right = dfs(curr.right)

            return
        
        dfs(root)
        
        return self.result



g = Solution()

root = root = [3,4,5,1,2]
root = list_to_tree(root)

subRoot = [4,1,2]
subRoot = list_to_tree(subRoot)
print(g.isSubtree(root, subRoot))




