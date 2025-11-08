'''
Problem name: Top K Frequent Elements

Link: https://leetcode.com/problems/top-k-frequent-elements/description/

Description: 
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

My thought process:
My approach was to count the occurences of each elements in a hashmap then store those in a list.
I then sorted the values of each and stored the sorted keys to another list. I then looped into
the value of k and returned the indices of the sorted array until the value of k.

Time & space complexity:
O(n + m^2 + n) time
O(n) space
'''

class Solution(object):
    def topKFrequent(self, nums, k):

        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] +=1
            else:
                dic[nums[i]] = 1
        keys = list(dic.keys())
        sorted_keys = []
        for key in keys:
            if not sorted_keys or dic[key] < dic[sorted_keys[len(sorted_keys)-1]]:
                sorted_keys.append(key)
            else:
                for i in range(len(sorted_keys)):
                    if dic[key] >= dic[sorted_keys[i]]:
                        sorted_keys.insert(i, key)
                        break
        result = []
        for i in range(k):
            result.append(sorted_keys[i])
        return result

g = Solution()

nums = [1]
k = 1
print(g.topKFrequent(nums, k))



'''

Kinda better structure:
Using for each loop for storing keys in a dictionary
using boolean check for when a loop has a chance of ending without doing anything, and it is also
inside another loop.
'''
class Solution(object):
    def topKFrequent(self, nums, k):

        dic = {}
        for num in nums:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1
        keys = list(dic.keys())
        sorted_keys = []
        
        for key in keys:
            inserted = False
            for i in range(len(sorted_keys)):
                if dic[k] > dic[sorted_keys[i]]:
                    sorted_keys.insert(i, key)
                    inserted = True
                    break
            if not inserted:
                sorted_keys.append(key)

        result = []
        for i in range(k):
            result.append(sorted_keys[i])
        return result




