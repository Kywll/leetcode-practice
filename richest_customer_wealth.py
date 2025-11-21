'''
Problem name: Richest Customer Wealth

Link: https://leetcode.com/problems/richest-customer-wealth/description/?envType=problem-list-v2&envId=array

Description: 
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

My thought process:
Just use nested for loops and compare which index is the highest.

Time & space complexity:
O(n^2) time
O(1) space

'''

class Solution(object):
    def maximumWealth(self, accounts):
        highest = 0
        for i in range(len(accounts)):
            current = 0
            for j in range(len(accounts[i])):
                current += accounts[i][j]
            if highest < current:
                highest = current
        return highest

g = Solution()

accounts = [[1,2,3],[3,2,1]]

print(g.maximumWealth(accounts))



