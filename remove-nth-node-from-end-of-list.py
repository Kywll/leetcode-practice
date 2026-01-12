'''
Problem name: Remove Nth Node From End of List

Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Description: 
Given the head of a linked list, remove the nth node from the end of the list and return its head.
My thought process:
My solution was to first reverse the linked list, then loop through it until you found the nth node.
You then just change the pointer of the prev of nth node into the next of nth node, effectively
removing the nth node. After that, just reverse the linked list again.

Time & space complexity:
O(n) time
O(1) space

What I learned:
After reversing a linked list, if we want to further manipulate it, you should consider making a 
new_head variable so that you are still able to track it after the pointer changes.
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
    def removeNthFromEnd(self, head, n):
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        new_head = prev
        curr = new_head
        prev = None

        i = 1
        while curr and i <= n:
            if i == n:
                if prev:
                    prev.next = curr.next
                else:
                    new_head = curr.next
                break
            prev = curr
            curr = curr.next
            i+=1

        curr = new_head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

obj = Solution()

head = [1,2,3,4,5]
n = 2

head = build_linked_list(head)

print(obj.removeNthFromEnd(head, n))






