'''
Problem name: Longest Substring Without Repeating Characters

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Description: 
Given a string s, find the length of the longest substring without 
duplicate characters.

My Thought Process:
I simply returned 0 if the length of the string is 0. I used two pointers and used a hashmap to check
duplicates. I first checked if the right pointer is equals to left pointer or already exists in the
hashmap, which I then simply just move the left pointer to the right and the right pointer to the 
position of the left pointer which would later get added 1 on. I also reset the hashmap and streak.
If it's not equals and does not exists in hashmap, then I simply add it to the hashmap and added 1 
to the streak.

Time & space complexity:
O(n) time
O(1) space
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        longest = 1
        
        l = 0
        r = 1

        streak = 1
        dic = {}
        while r <= len(s)-1:
            
            if s[r] in dic or s[r] == s[l]:
                l +=1
                r = l
                dic = {}
                streak = 1
            else:
                dic[s[r]] = r
                streak+=1
                longest = max(streak, longest)

            r+=1

        return longest


g = Solution()

s = "pwwkew"

print(g.lengthOfLongestSubstring(s))