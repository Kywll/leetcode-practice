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





'''
Optimized and proper sliding window solition:

Thought Process:
I used a proper sliding window approach, and used a set to determine if there are any duplicates.
I first checked if the right pointer has a duplicate already in the set, which I then checked in
a loop if the left pointer is equals to the right or not, if it is, I just removed the left pointer
because it's no longer part of the window, then at the end I just moved the left pointer to the right
once it's equals to the right pointer and didn't need to remove the left pointer because the right 
pointer is equals to it and should be included in the set. If in case that the right pointer is not 
a duplicate, I just add it to the set. At the end of each iteration, I just update the longest 
substring based on the length of the set.


Complexity:
O(n) time
O(m) space

What I learned:
I learned that I could use a nested loop using a sliding window technique and still get a linear
time as long as the pointers are moving in one direction. I also learned that a set is useful
when I simply want to check if a duplicate already exists without the need for extra space for
keys.


'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        longest = 1
        charSet = set()
        charSet.add(s[0])

        l = 0
        for r in range(1, len(s)):
            if s[r] in charSet:
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l+=1
                l+=1
            else:
                charSet.add(s[r])
            longest = max(longest, len(charSet))

        return longest


g = Solution()

s = "abba"

print(g.lengthOfLongestSubstring(s))



'''
Standard Solution:

Thought Process:
Basically allows you to no longer check a lot of cases manually. It besically just checks first
if there is a duplicate which you just keep removing the left pointer or shrink the sliding window
until a duplicate no longer exist in the set. Otherwise you just simply add the right pointer
to the set then update the longest substring based on set length.

What I learned:
I could just start the right pointer at the start of the array, and I could simply check the right 
right pointer and update the left pointer until it checks out.

'''



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        charSet = set()

        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            charSet.add(s[r])
            longest = max(longest, len(charSet))

        return longest


g = Solution()

s = "abba"

print(g.lengthOfLongestSubstring(s))