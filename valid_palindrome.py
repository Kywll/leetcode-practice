'''
Title: Valid Palindrome

Link: https://leetcode.com/problems/valid-palindrome/

Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

My Thought Process:

What I learned:
When doing a two pointer and approaching from opposite sides, it is better
to compare if i is less than j so you could prevent it from exceeding each
immediately other which would look like While i < j: This would prevent it 
from running compared to != which would still run because it's still true
if they are equals which is not what you want.


Time & space complexity:
O(n) time
O(n) space

'''

class Solution(object):
    def isPalindrome(self, s):
        result = ""
        for string in s.lower():
            if string.isnumeric():
                if int(string) >= 0 and int(string) <= 9:
                    result += string
            elif str(string) >= "a" and str(string) <= "z":
                result += string
        reversed = list(result)
        i = 0
        j = len(result)-1
        while i < j:
            temp = reversed[i]
            reversed[i] = reversed[j]
            reversed[j] = temp
            i+=1
            j-=1
        reversed = "".join(reversed)
        if result == reversed:
            return True
        return False
    
g = Solution()

s = "0P"
print(g.isPalindrome(s))



