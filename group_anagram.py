
'''
Title: Group Anagrams

Link: https://leetcode.com/problems/group-anagrams/description/

Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
My Thought Process:
My approach was to loop through the array and check if a string in the array already exists
in the dictionary if it's sorted and joined together. If it does, then just append the index to 
the list value of that key. If not, then create a new key and insert the index in a list form
so you could append later. After that, I stored all the keys in a variable and turned it into
an array. I theniterated through each keys and then appened the current list index of the said 
key into a list I created named result. This is done so that the length of the list value in the
dictionary keys will be inserted to the result which would allow me to determine the length of
each array elements inside the result. I then looped through it and changed the elements of the
current list inside the result into the index list of the current key in the dictionary which
I also iterated through.


Time & space complexity:
O(n log n) depending on sorting algo
O(1)

'''

class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for i in range(len(strs)):
            new = "".join(sorted(strs[i]))
            if new in dic:
                dic[new].append(i)
            else:
                dic[new] = [i]
        keys = list(dic.keys())
        result = []
        i = 0
        for s in keys:
            result.append(dic[s])
            for j in range(len(dic[s])):
                result[i][j] = strs[dic[s][j]]         
            i+=1
        return result
        

g = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
print(g.groupAnagrams(strs))


