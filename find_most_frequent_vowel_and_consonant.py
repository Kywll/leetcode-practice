'''
Problem name: Find Most Frequent Vowel and Consonant

Link: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/?envType=problem-list-v2&envId=string

Description: 
You are given a string s consisting of lowercase English letters ('a' to 'z').

Your task is to:

Find the vowel (one of 'a', 'e', 'i', 'o', or 'u') with the maximum frequency.
Find the consonant (all other letters excluding vowels) with the maximum frequency.
Return the sum of the two frequencies.

Note: If multiple vowels or consonants have the same maximum frequency, you may choose any one of them. If there are no vowels or no consonants in the string, consider their frequency as 0.

The frequency of a letter x is the number of times it occurs in the string.
 

My Thought Process:
My thought process was to make two hashmaps, one for vowel and one for consonant. I already declared 
vowels and put b as a placeholder for the top cons while I just chose a as placeholder for top vowel.
I then looped through the array and checked if it's a vowel, and if it is, I just add 1 to the 
hashmap key and compare it to the top vowel and just replace if yes. If it's not a vowel, I just put
a key if it does not already exist, otherwise just add it in the hashmap and after that, I check if 
it's greater than top cons or not which I just do the same process of replacing top con if the
current letter is greater, otherwise just move on. At the end, I just returned the sum of top vowel
and top con frequencies.

Time & space complexity:
O(n) time
O(1) space


'''


class Solution(object):
    def maxFreqSum(self, s):
        vowel = {"a":0, "e":0, "i":0, "o":0, "u":0}
        cons = {"b":0}
        top_vowel = "a"
        top_cons = "b"

        for letter in s:
            if letter in vowel:
                vowel[letter] +=1
                if vowel[letter] >= vowel[top_vowel]:
                    top_vowel = letter
            else:
                if letter in cons:
                    cons[letter] +=1
                else:
                    cons[letter] = 1
                if cons[letter] >= cons[top_cons]:
                    top_cons = letter
        return vowel[top_vowel] + cons[top_cons]
    
g = Solution()

s = "successes"

print(g.maxFreqSum(s))
