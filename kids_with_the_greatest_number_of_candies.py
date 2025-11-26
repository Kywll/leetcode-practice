'''
Problem name: Kids With the Greatest Number of Candies

Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=problem-list-v2&envId=array


Description: 
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

My Thought Process:
Loop through the array first to find the highest amount of candies in the array then loop again outside and
compare the added value of the current index with the extra candies and return True if it's equal or greater
than the max amount of candies, otherwise just return false.

Time & space complexity:
O(n) time
O(1) space

'''

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result = []

        max_candies = 0

        for candy in candies:
            if candy > max_candies:
                max_candies = candy
        for candy in candies:
            if (candy + extraCandies) >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result


g = Solution()
candies = [2,3,5,1,3]
extraCandies = 3

print(g.kidsWithCandies(candies, extraCandies))