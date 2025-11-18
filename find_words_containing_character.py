'''
Problem name: Find Words Containing Character

Link: https://leetcode.com/problems/find-words-containing-character/description/?envType=problem-list-v2&envId=array

Description: 
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

My thought process:
The bruteforce solution is to simply just loop though the list and the list 
elements.

Time & space complexity:
O(n^2) time
O(1) space

'''

class Solution(object):
    def findWordsContaining(self, words, x):
        result = []
        for i in range(len(words)):
            for letter in words[i]:
                if letter == x:
                    result.append(i)
                    break
        return result

g = Solution()

words = ["leet","code"]
x = "e"

print(g.findWordsContaining(words, x))


'''
My thought process:


Time & space complexity:
O(n) time
O(1) space

'''


class Solution(object):
    def findWordsContaining(self, words, x):
        result = []
        for i in range(len(words)):
            if x in set(words[i]):
                result.append(i)
        return result

g = Solution()

words = ["leet","code"]
x = "e"

print(g.findWordsContaining(words, x))
