'''
Problem name: Reorder List
Link: https://leetcode.com/problems/reorder-list/description/

Description: 
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.


My thought process:
The idea is to first find the middle of the linked list by using a slow and fast pointer technique
and then determining the left side and right side of the linked list. The next step is to reverse the
right side, so that you can just merge the linkedlist in an alternating pattern which is what the
goal is. To merge the 2 sides, we first store the next values of each then make the pointer of 
left into the right pointer so you can have it in alternate, then you turn the pointer of right
into l_next which makes the overall value of the list looks like: 1(L)->5(R)->(LN)2->3. Then you
do right = l_next which basically makes you jump into 2(LN), PS: 1-5 is still kept and still points to 
2. And do right = 4(RN). On the next iteration, you turn the value of LN into the next of left which
is 3, then RN into next of 4, which is None. Then you turn the pointer of left into the right, so
now it looks like 1->5->2(L)->4(R)->None. Then you turn the pointer of right into l_next which is 
3->None. So the final look is now 1->5->2(L)->4(R)->3(LN)->None. At the end, you turn the value of
Right into LN which is 3, and value of right into RN which is None, so the loop ends.

Time & space complexity:
O(n) time
O(1) space

What I learned:
I learned that we can find the middle of a linked as well as the left side and right side by using
slow and fast pointers, this works because fast pointer traves 2 times faster than slow pointer, so 
by the time that fast pointer reaches the end of the list, then slow is still on the middle of it
because len(list) / 2 is the half. I also learned to only track pointer changes and how changing 
the pointer of something and then changing the pointer of the pointer you changed with will affect
the final list, And if you stored a pointer, even if the pointers and heads got adjusted, it will
still point to that pointer after the changes. I think it's a good idea to always have a visual model
of the final result.
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
    def reorderList(self, head) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        left = head
        right = prev
        while right:
            l_next = left.next
            r_next = right.next

            left.next = right
            right.next = l_next

            left = l_next
            right = r_next

        



            
obj = Solution()

head = build_linked_list([2,4,6,8])

print(obj.reorderList(head))

