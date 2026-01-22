'''
Problem name: Diameter of Binary Tree

Link: https://leetcode.com/problems/diameter-of-binary-tree/description/

Description: 
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

My thought process:

Time & space complexity:

'''



'''
Problem name: Diameter of Binary Tree

Link: https://leetcode.com/problems/diameter-of-binary-tree/description/

Description: 
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

My Thought Process:
The idea was the you could find the diameter of a node by simply just adding the the height of each 
child, however we can't really store it during recursion so we used a global variable outside the 
recursion. there are also times where when splitting branches and they are uneven, then it creates
different diameter for each nodes where the root node might not necessarily have the most diameter
becuase a deeper node went past a chidren of the root node, so what we do is just compare if the 
current node has more diameter than the other nodes and just return the highest one because that is 
the max possible diameter of the tree.

Time & space complexity:
O(n) time
O(n) space

What I learned:
I learned that we can use a global variable if we need to store information while doing a recursion.
I also learned that we could find the diameter of a tree based on it's height.

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
    def diameterOfBinaryTree(self, root):
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return max(left, right) + 1
        
        dfs(root)
        return self.res
    
g = Solution()

root = [1,2,3,4,5]
root = list_to_tree(root)
print(g.diameterOfBinaryTree(root))




