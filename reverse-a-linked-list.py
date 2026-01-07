'''
Problem name: Reverse Linked List

Link: https://leetcode.com/problems/reverse-linked-list/description/

Description: 
Given the head of a singly linked list, reverse the list, and return the reversed list.

My thought process:
The idea is to store the prev and curr values and keep looping until you the last values is reached.
The solution is to first store the next val of current into a temp var and then setting the next
of current into the prev val or the head val of curr. Then the curr value becomes the next val which 
is the value stored in the temp var, and the curr becomes the prev. Basically just keep re routing
the next values of each of them to the left or the head.

Time & space complexity:
O(n) time
O(1) space

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
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


obj = Solution()

head = build_linked_list([1,2,3,4,5])


print(obj.reverseList(head))