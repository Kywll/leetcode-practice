'''
Problem name: Merge Two Sorted Linked Lists

Link: https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150

Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

My thought process:
The idea is to sotre the current and the next values of both lists and just compare them to each 
other and place the lower one to the result and make the current into the next and the next into the
next of the new current, once a list has no more next values, you simply just use a loop and append
the leftover values of the other one to the result.

Time & space complexity:
O(n + m) time
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
    def mergeTwoLists(self, list1, list2):
        result = ListNode()
        r = result

        c1 = list1
        c2 = list2

        if c1:
            n1 = c1.next
        if c2:
            n2 = c2.next

        while c1 or c2:
            if c1 and c2:
                if c1.val > c2.val:
                    r.next = c2
                    c2 = n2
                    if n2 is not None:
                        n2 = n2.next
                elif c1.val <= c2.val:
                    r.next = c1
                    c1 = n1
                    if n1 is not None:
                        n1 = n1.next
                r = r.next
            elif c1:
                while c1:
                    r.next = c1
                    r = r.next
                    c1 = n1
                    if n1 is not None:
                        n1 = n1.next
            else:
                while c2:
                    r.next = c2
                    r = r.next
                    c2 = n2
                    if n2 is not None:
                        n2 = n2.next

        return result.next


head1 = build_linked_list([1,2,4])
head2 = build_linked_list([1,3,5])

obj = Solution()


print(obj.mergeTwoLists(head1, head2).next.val)


'''
Cleaner Solution:

Thought Process:
The idea is to simply just use a dummy and a tail at the start and just loop through the parameters
directly instead of using variables for it. After comparing and making the value of the tail next into 
the list, we make the list into the next of it. Then at the end, we just put the value of tail into
it's next so we can change that after instead. Then at the end just turn the list itself into the
next of tail because it will simply point to the leftovers.

'''


class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next


head1 = build_linked_list([1,2,4])
head2 = build_linked_list([1,3,5])

obj = Solution()


print(obj.mergeTwoLists(head1, head2).val)