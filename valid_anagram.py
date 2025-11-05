'''
Title: Valid Anagram

Link: https://leetcode.com/problems/valid-anagram/description/

Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

My Thought Process:
Since the problem is simply looking if 2 arrays are an anagram of each other, then we can simply
just sort them and and compare if each value is equals and if not just return False. Check at 
the start if their lengths are equals because if not, then you reutrn False because it's 
impossible for them to be anagram of each other due to them not having the same amount of numbers.



Time & space complexity:
O(n log n) depending on sorting algo
O(1)

'''


class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        sortedS = sorted(s)
        sortedT = sorted(t)
        for i in range(len(s)):
            if sortedS[i]!= sortedT[i]:
                return False
        return True

g = Solution()

s = "anagram"
t = "nagaram"

print(g.isAnagram(s, t))



