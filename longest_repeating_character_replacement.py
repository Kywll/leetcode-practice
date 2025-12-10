'''
Problem name: Longest Repeating Character Replacement

Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/

Description: 
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

My Thought Process:

Time & space complexity:

'''

class Solution(object):
    def characterReplacement(self, s, k):
        if len(s) == 0:
            return 0
        longest = 0
        l = 0
        r = 1
        
        for l in range(len(s)-1):
            streak = 1
            cur_k = k
            for r in range(l, len(s)-1):
                if s[l] != s[r]:
                    cur_k -=1
                streak+=1
                longest = max(longest, streak)
                if cur_k < 1:
                    break
    
        return longest
    
g = Solution()

s = "ABAB"
k = 2
print(g.characterReplacement(s, k))







'''
streak = 1
cur_k = k
while cur_k >= 0 and r <= len(s)-1:
    print([s[r]])
    if s[l] != s[r]:
        cur_k -=1
    streak +=1
    longest = max(streak, longest)

    if cur_k <= 0:
        l +=1
        cur_k = k
        streak = 1
        r = l
    r+=1
'''