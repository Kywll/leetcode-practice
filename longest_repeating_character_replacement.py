'''
Problem name: Longest Repeating Character Replacement

Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/

Description: 
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

My Thought Process:
The approach was to use a sliding window technique where I put the characters on a hashmap and
then count their frequencies so far. I then calculated the length of the window minus the key of 
the hashmap that has the highest value. This works because once we calculated that, we can simply
check if it's greater than k, which means that we skipped too much letters and is now over what
is allowed to be changed.

Time & space complexity:
O(n) time
O(1) space

What I learned:
I learned that a sliding window technique should actually be followed because it's easier to
visualize that way when you are following the window visual. It will then all matter on your 
computation and how you shrink the window, basically just increase the size of the window until the 
end and always check if the window should be shrinked or not.

'''

class Solution(object):
    def characterReplacement(self, s, k):
        if not s:
            return 0
        dic = {}
        longest = 0
        l = 0

        most_freq = s[0]
        for r in range(len(s)):
            if s[r] in dic:
                dic[s[r]] +=1 
            else:
                dic[s[r]] = 1 
            if dic[most_freq] < dic[s[r]]:
                most_freq = s[r]
            if ((r-l)+1) - dic[most_freq] <= k:
                longest = max(longest, ((r-l)+1))
            else:
                dic[s[l]] -=1
                l+=1

        return longest
    
g = Solution()

s = "ABAB" 
k = 2
print(g.characterReplacement(s, k))




