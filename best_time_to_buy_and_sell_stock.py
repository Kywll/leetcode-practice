'''
Problem name: Best Time to Buy and Sell Stock

Link: https://leetcode.com/problems/build-array-from-permutation/description/?envType=problem-list-v2&envId=array

Description: 
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

My thought process:
Just use a nested loop and compare the highest j-i values then return it at the end

Time & space complexity:
O(n^2) time
O(1) space

'''

class Solution(object):
    def maxProfit(self, prices):
        highest = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > highest:
                    highest = prices[j] - prices[i]
        return highest


g = Solution()

prices = [7,6,4,3,1]

print(g.maxProfit(prices))





