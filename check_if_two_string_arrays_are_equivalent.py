'''
Problem name: Check If Two String Arrays are Equivalent

Link: https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/?envType=problem-list-v2&envId=array

Description: 
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

My Thought Process:
Simply combine the array of strings into a single string and compare the two
words from each other.

Time & space complexity:
O(n) time
O(n) space


'''


class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        final_word1 = ""
        final_word2 = ""

        for word in word1:
            final_word1 += word
        for word in word2:
            final_word2 += word
        
        if final_word1 == final_word2:
            return True
        return False

g = Solution()

word1 = ["ab", "c"]
word2 = ["a", "bc"]

print(g.arrayStringsAreEqual(word1, word2))








