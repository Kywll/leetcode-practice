'''
Problem name: Copy List with Random Pointer

Link: https://leetcode.com/problems/copy-list-with-random-pointer/description/


Description: 
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

My Thought Process:
The idea was to make a hashmap to store the copy of each nodes on the linked list. We do this by
deep copying each node first by doign copy = Node(curr.val), this is done so that we can ensure
that the copy is actually a copy and not just a reference to the original node, Then, we store
the copied value into the hashmap with the original node as the key. Next, we now loop through the 
linkedlist and call the copy of the current value from the hashmap. We then, determine the next and
random pointers of the copy node of the current node, we do this with copy.next = oldToCopy[curr.next] 
and copy.random = oldToCopy[curr.random]. This is done because the nodes inside the hashmap has no 
wired pointers, basically they are lone nodes, so you access them using the original node as the key 
because it uniquely identifies which copied node we want.. Then just return the copy of the head from 
the hashmap with it's now correct pointers.

Time & space complexity:
O(n) time
O(n) space

What I learned:
I learned that doing a deep copy of node requires you to do Node(curr.val) which means that it has
no pointers. We can use a hashmap to create a copy of nodes and allow us easily find those nodes
in constant time, this is important because those copied nodes have nothing pointing to them so 
using a hashmap let's you find it by just knowing the original. I also learned that if you
store a node as value on a hashmap, you still have it's pointers.
'''




class Solution:
    def copyRandomList(self, head):
        oldToCopy = {None: None}
        curr = head
        
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]

g = Solution()

head = [[7,None],[13,0],[11,4],[10,2],[1,0]]

print(g.copyRandomList(head))


