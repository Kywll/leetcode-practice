'''
Problem name: Minimum Window Substring

Link: https://neetcode.io/problems/minimum-window-with-characters/question

Description:
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

My thought process:
The thought behind the solution was to first store the keys and frequencies of t in a hashmap, then we take a variable have which will track how many keys are matched with need(the length of t).
We used a sliding window approach where we move the right pointer until we are able to get a substring that satifies all frequencies in t. Then we increment the have variable and store the
length of the substring to the result if less than the previous one. Once the have variable is equals to the need variable, we simply just loop and reduce the size of the window until it's no longer equals.

Time & space complexity:
O(n) time
O(k) space



What I learned:
I learned how to use match counting whenever you want to check frequencies on a hashmap but some of them could be greater than the other while still requiring to atleast meet the minimum.
I also learned to be more careful of choosing my invariant.

'''



class Solution(object):
    def minWindow(self, s, t):
        if t == "":
            return ""
        
        countT, window = {}, {}

        for c in t:
            if c in countT:
                countT[c] +=1
            else:
                countT[c] = 1
        
        
        have, need = 0, len(countT)
        result = ""

        l = 0

        for r in range(len(s)):
            c = s[r]
        
            if c in window:
                window[c] +=1
            else:
                window[c] = 1

            if c in countT and window[c] == countT[c]:
                have+=1

            while have == need:
                if len(s[l:r+1]) < len(result) or result == "":
                    result = s[l:r+1]

                window[s[l]] -=1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
                
        return result
        



g = Solution()

s = "ADOBECODEBANC" 
t = "ABC"
print(g.minWindow(s, t))









