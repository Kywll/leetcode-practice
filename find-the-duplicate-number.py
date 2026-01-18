'''
Problem name: Find the Duplicate Number

Link: https://leetcode.com/problems/find-the-duplicate-number/description/

Description: 
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

My thought process:
The idea was to just use a set to check if there is a duplicate.

Time & space complexity:
O(n) time
O(n) space

'''

class Solution:
    def findDuplicate(self, nums):
        empty_set = set()

        for num in nums:
            if num in empty_set:
                return num
            else:
                empty_set.add(num)

g = Solution()

nums = [1,3,4,2,2]

print(g.findDuplicate(nums))

'''
OPTIMAL SOLUTION:
The idea was to traverse the linked list with a fast an slow pointer and stop until they meet.
After doing so, you create another slow pointer and then traverse the linkedlist again using the
new slow pointer alow with the old slow pointer and stop until they meet then return either of them
because that means that once after they meet, then that means that there was a duplicate and they
point to the same node.

TIME COMPLEXITY:
O(n) time
O(1) space

WHAT I LEARNED:
Traversing nodes using slow and fast pointer until they meet can return if there was a cycle. But
creating another slow pointer and traversing the linkedlist again using the new slow pointer along
the original slow pointer would let you find the actual node that forms the cycle(The one that
has multiple nodes pointing it)
'''

class Solution:
    def findDuplicate(self, nums):
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

g = Solution()

nums = [1,3,4,2,2]

print(g.findDuplicate(nums))

