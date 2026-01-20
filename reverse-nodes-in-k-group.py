'''
Problem name: Reverse Nodes in k-Group

Link: https://leetcode.com/problems/reverse-nodes-in-k-group/description/

Description: 
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

My thought process:
The idea was to first make a dummy node so you could have a pointer to the final head. The next is to
have a k pointer traverse the linkedlist until you get the the kth node. Then you store the next of it
as the group_next. After that, you can now reverse the group_prev which is the nodes until kth node 
have prev as group_next because you want the first node of the group_prev to point to it because
it will be the end after reversing. After reversing, you now want to make a temp var that is equals
to the next of group_prev which is the last node of the group_prev because you never actually changed
that pointer before so it still points to the previous first node. Then you point the group_prev to
the kth node(the first node now, at the first iteration this is simply pointing the dummy node to
it's head, but at the next iteration, it's pointing the last of group_prev into the new starting node
of the group_next). Then set group_prev into so now you have group_prev pointing at the start of
group_next.

Time & space complexity:
O(n) time
O(1) space

What I learned:
When the original head changes, it's better to just have a dummy node that points to the original
head then just change that along the way. 
Linked list problems are about anchoring, not reversing. The reversal itself is easy. What kills you 
is losing where you came from and where you’re going. Key anchors you must have before touching 
pointers:
Node before the group
First node of the group
Last node of the group
Node after the group

If any of these aren’t named and frozen → bugs are guaranteed.

Reverse while curr is almost always a red flag. When a problem says: reverse k nodes then:
while curr: is wrong
while curr != boundary: is right
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next

    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_next = kth.next

            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
            
            

g = Solution()

head = [1,2,3,4,5]
k = 3
head = build_linked_list(head)


print_linked_list(g.reverseKGroup(head, k))

