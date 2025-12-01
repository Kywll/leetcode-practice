
'''
Problem name: Reverse Words in a String III
Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/?envType=problem-list-v2&envId=string

Description: 
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

My thought process:
I simply stored the words that was splitted in a variable then looped through it and checked if 
it's the last word, if not then just the value of result into result + reversed word + space. If yes,
do the same thing but with no space in the end.

Time & space complexity:
O(n) time
O(n space)


'''



class Solution(object):
    def reverseWords(self, s):
        result = ""
        words = s.split(" ")
        for i in range(len(words)):
            if i != len(words)-1:
                result = result + words[i][::-1] + " "
            else:
                result = result + words[i][::-1]

        return result
    
g = Solution()
s = "Let's take LeetCode contest"
print(g.reverseWords(s))