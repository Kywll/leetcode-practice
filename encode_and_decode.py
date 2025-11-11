'''
Problem name: Encode & Decode

Link: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150

Description: 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

My thought process:
The firs thing that we need to figure out is a way to determine the delimeter for the encoded string. What we came up with
is putting the length of the string at the start and a # sign next to it before the strings. This way, we can simply
iterate through the encoded string, and stop once we find a # sign which is immediately because it's right at the start, 
then check the previous index to know how long the string is, then just decode the indexes next to the # sign so until
the length is reached which we can know by looking at the number before the # sign. This is done so that in case there
is a # sign in between the strings, it won't matter because we're not even checking it. This was also done by simply using
a while loop for i and j being equals to i, you then using another while loop to check the # sign, which you then make the
value of i into the end of the word which is equals to the next index after # plus the length of the word which is the number
before the # sign, that way we just jump to the next word and won't need j to iterate over every index because if it did,
there is a chance that it will find a # sign inside the words if it exists and it would break the code.

Time & space complexity:
O(n * L) time and space
'''

class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            
            res.append(s[j+1: j+1+length])
            i= j+1+length
        return res

g = Solution()

sample = ["neet","code","love","you"]

encoded = g.encode(sample)
print(g.decode(encoded))


