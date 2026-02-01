'''
Problem name: Same Tree

Link: https://leetcode.com/problems/same-tree/description/

Description: 
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

My Thought Process:
The idea was to compare the 2 roots using a bfs together and compare them side by side then return False once you saw
that they are not equals, otherwise return True at the end.

Time & space complexity:
O(n) time
O(n) space

What I Learned:
If you want to check 2 nodes if they either one of them is none and if they are the same value, basically if you want to 
know if they are equals. You can just check first at the top if both of them are None then you just continue, then check
if one of them is None(that means you can return False). Then compare their values at the end(you can safely do so now
because you already checked if there was None). I also learned that you could perform bfs on two different roots and
be able to compare them side by side.
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
    def isSameTree(self, p, q):
        def bfs(p, q):
            queueP = [p]
            queueQ = [q]

            i = 0
            while i < len(queueP) and i < len(queueQ):
                if not queueP[i] and not queueQ[i]:
                    i+=1
                    continue
                
                if not queueP[i] or not queueQ[i]:
                    return False

                if queueP[i].val != queueQ[i].val:
                    return False
                
                queueP.append(queueP[i].left)
                queueP.append(queueP[i].right)

                queueQ.append(queueQ[i].left)
                queueQ.append(queueQ[i].right)
                
                i+=1
            
            return True
            
        return bfs(p, q)



g = Solution()

p = [1,2,3]
q = [1,2,3]
p = list_to_tree(p)
q = list_to_tree(q)
print(g.isSameTree(p, q))
