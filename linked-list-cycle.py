'''
Problem name: Linked List Cycle

Link: https://leetcode.com/problems/linked-list-cycle/description/

Description: 
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

My Thought Process:
The idea is to just check if there is a duplicate between the linked list values. This is done by 
using a hash set and just checking if there the current val of linked list is inside, if not then just
append it.

Time & space complexity:
O(n) time
O(n) space
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

class Solution:
    def hasCycle(self, head) -> bool:
        tail = head

        empty_set = set()

        while tail:
            if tail in empty_set:
                return True
            empty_set.add(tail)
            tail = tail.next

        return False

head = [3,2,0,-4]
pos = 1

head = build_linked_list([3,2,0,-4])

obj = Solution()

print(obj.hasCycle(head))
