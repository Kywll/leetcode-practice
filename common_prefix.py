'''
- Problem name: Longest Common Prefix
- Description: 
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

- My thought process:
    To solve this problem, I first placed the first string to an array named result in order to
    compare that to the other strings then removed the first string from the original array 
    since I don't need it anymore. I used a for each loop to get the values of each string in 
    the array then I used a while loop inside to compare if the index of the current string is 
    the same as the index of the result. If the index of the result and the current string is
    not the same, then I just cut off the result value until the index that was the same as the
    index of the current string. After the inner loop, I then cut the result until the last 
    value of i in the inner loop so that if the current string is shorter, then the result will
    be cut as well since that automatically means that they can never be the same due to one
    being shorter than the other
- Time & space complexity:
    O(n^2) time complexity
    O(n) space

'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        result = strs[0]
        strs.pop(0)
        for str in strs:
            i=0
            while i < len(str) and i < len(result):
                if str[i] != result[i]:
                    result = result[:i]
                i+=1
            result = result[:i]
        return result
    
strs = ["flower","flow","flight"]
g = Solution()

print(g.longestCommonPrefix(strs))



