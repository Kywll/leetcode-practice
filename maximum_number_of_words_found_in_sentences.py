'''
Problem name: Maximum Number of Words Found in Sentences

Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/?envType=problem-list-v2&envId=string

Description: 
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.

My Thought Process:
Basically just loop through the array and get the number of words of current sentence by using split()
and comparing it with max variable. 

Time & space complexity:
O(n) time
O(1) space

'''

class Solution(object):
    def mostWordsFound(self, sentences):
        max = 0
        for sentence in sentences:
            current = len(sentence.split(" "))
            if current > max:
                max = current
        return max
            

g = Solution()
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

print(g.mostWordsFound(sentences))


