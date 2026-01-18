'''
Problem name: Merge K Sorted Linked Lists

Link: https://leetcode.com/problems/merge-k-sorted-lists/description/

Description:
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

My thought process:
The idea was to loop through all the nodes and store them all in a heap while also connecting all the
nodes on the list to each other so that all the nodes are connected. After doing that, you have 
exactly the size of all the nodes in the list so you can simply just assign the values of min
heap the them.


Time & space complexity:
O(n log n) time
O(n) space


'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:    
    def mergeKLists(self, lists):
        import heapq
        result = ListNode()
        tail = result

        heap = []
        for head in lists:
            tail.next = head
            while head:
                tail = tail.next
                count +=1
                heapq.heappush(heap, head.val)
                head = head.next

        result = result.next
        tail = result
        while tail:
            tail.val = heapq.heappop(heap)
            tail = tail.next
        
        return result


lists = [[1,4,5],[1,3,4],[2,6]]

g = Solution()

print(g.mergeKLists(lists))