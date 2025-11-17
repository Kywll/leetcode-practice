'''
Problem name: Restore Finishing Order

Link: https://leetcode.com/problems/restore-finishing-order/description/?envType=problem-list-v2&envId=array
Description: 
You are given an integer array order of length n and an integer array friends.

order contains every integer from 1 to n exactly once, representing the IDs of the participants of a race in their finishing order.
friends contains the IDs of your friends in the race sorted in strictly increasing order. Each ID in friends is guaranteed to appear in the order array.
Return an array containing your friends' IDs in their finishing order.

My thought process:
Just store in hashmap and loop through to the order aray and store each one
that is a key in the dictionary.

Time & space complexity:
O(n + m) time
O(n) space
'''

class Solution(object):
    def recoverOrder(self, order, friends):
        dic = {}
        result = []
        for friend in friends:
            dic[friend] = friend
        for num in order:
            if num in friends: 
                result.append(num)
        return result
                

g = Solution()

order = [3,1,2,5,4]
friends = [1,3,4]

print(g.recoverOrder(order, friends))





