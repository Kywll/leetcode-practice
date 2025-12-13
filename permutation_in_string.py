'''
Problem name: Permutation in String

Link: https://leetcode.com/problems/permutation-in-string/description/

Description:
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

My thought process:
I simply used a pointer approach and stored the frequencies of s1 in a hashmap. I then looped
through s2 and checked whether the length of the window is the same as the lenght of s1 which if not,
I just keep adding to the right pointer and increasing the size of the window while adding the 
frequencies at the same time. After that, I check if an equal permutation was found which I just 
simply return. If not then I just checked if the left pointer value has only one frequency, which I 
then just removed if yes, otherwise reduce one. Then at the end of the iteration, I added one
to the left pointer which would make the window size shorter than s1 whcih will then repeat the 
process of moving the right pointer and expanding the window size.

Time & space complexity:
O(n) time
O(1) space due to alphabets being limited

'''

class Solution(object):
    def checkInclusion(self, s1, s2):
        dic1 = {}
        for s in s1:
            if s in dic1:
                dic1[s] +=1
            else:
                dic1[s] = 1

        dic2 = {}
        l = 0
        r = 0
        while r <= len(s2)-1:
            while r <= len(s2)-1 and ((r-l)+1) <= len(s1):
                if s2[r] in dic2:
                    dic2[s2[r]] +=1
                else:
                    dic2[s2[r]] = 1
                r+=1

            if dic1 == dic2:
                return True
            if dic2[s2[l]] <= 1:
                del dic2[s2[l]]
            else:
                dic2[s2[l]]-=1

            l+=1
        
        return False

g = Solution()

s1 = "ab"
s2 = "eidboaoo"

print(g.checkInclusion(s1, s2))
