


'''
Problem name: Koko Eating Bananas

Link: https://leetcode.com/problems/koko-eating-bananas/description/

Description: 
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

My Thought Process:
The thought process was that the possible numbers of amounts of banana eaten per hour starts from 1
until the max of piles. So what we need to do is to use binary search into that range and then check
if it is viable by simply looping through the array and checking if the current middle selected 
is able to eat all bananas in the pile at the time given. This is done by using ceil division or 
doing amount of current pile + mid -1 // mid basically we want to find how many times the current mid
has to repeat to become greater or equals the the piles[i]. Then we compare if it's greater than the
maximum time available where we simply just ignore it and look at the range of numbers at the right
of mid and do binary search again, otherwise the mid becomes the asnwer, and we do binary search at 
the left to find even smaller possible times 

Time & space complexity:
O(log(max(p)) * P) time
O(1) space

What I learned:
Binary search can be applied not only to arrays, but also to abstract answer spaces when the problem 
has a monotonic condition.

'''

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right

        while left <= right:
            mid = (left+right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid -1) // mid

            if hours > h:
                left = mid+1
            elif hours <= h:
                answer = mid
                right = mid-1
            
        return answer





g = Solution()

piles = [30,11,23,4,20]
h = 5

print(g.minEatingSpeed(piles, h))




