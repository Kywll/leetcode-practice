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



'''
Hashmap Solution

My Thought Process:
For a more faster way of solving, you can simply just create hashmaps for both and use the 
characters as key on the hashmap and count their occurrences then compare it. If it's not the 
same, then return false, but if the loop ends, then return True since that means all character
occurrences are equals and they are an anagram of each other.

Time & space complexity:
O(n)
O(1)
'''

class OtherSolution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        dicS = {}
        dicT = {} 
        for i in range(len(s)):
            if s[i] in dicS:
                dicS[s[i]] +=1
            else:
                dicS[s[i]] = 1
            if t[i] in dicT:
                dicT[t[i]] +=1
            else:
                dicT[t[i]] = 1
        key_of_s = list(dicS.keys())
        for k in key_of_s:
            if dicS[k] != dicT[k]:
                return False
        return True

g = OtherSolution()

s = "anagram"
t = "nagaram"

print(g.isAnagram(s, t))




