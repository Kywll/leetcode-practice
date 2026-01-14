'''
Problem name: Add Two Numbers

Link: https://leetcode.com/problems/add-two-numbers/description/

Description: 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

My thought process:
I simply just stored the values in a string at reverse then added them together. Finally I looped
through the added string in reverse and built a linkedlist on each iteration. 

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
    def addTwoNumbers(self, l1, l2):
        result = 0

        l1_num = ""
        l2_num = ""
        while l1 or l2:
            if l1:
                l1_num = str(l1.val) + l1_num
                l1 = l1.next
            if l2:
                l2_num = str(l2.val) + l2_num
                l2 = l2.next
            
        result = str(int(l1_num) + int(l2_num))

        final_result = ListNode(0)
        dummy = final_result
        
        for i in range(len(result)-1, -1, -1):
            dummy.next = ListNode(int(result[i]))
            dummy = dummy.next

        return final_result.next


        
l1 = [2,4,3]
l2 = [5,6,4]

l1 = build_linked_list(l1)
l2 = build_linked_list(l2)

g = Solution()

print(g.addTwoNumbers(l1, l2).val)





