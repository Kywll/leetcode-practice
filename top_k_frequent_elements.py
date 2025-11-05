'''
Problem name: Top K Frequent Elements

Link: https://leetcode.com/problems/top-k-frequent-elements/description/

Description: 
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

My thought process:

Time & space complexity:

'''


class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        uniques = []
        if len(nums) == 1:
            uniques.append(nums[0])
            return uniques

        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] +=1
            else:
                dic[nums[i]] = 1
                uniques.append(nums[i])
        values = []
        for i in range(len(uniques)):
            values.append(dic[uniques[i]])
        final = []
        for i in range(1, len(values)):
            if len(final) < k:
                if values[i] > values[i-1]:
                    final.append(uniques[i])
                else:
                    final.append(uniques[i-1])
            else:
                if values[i] > values[i-1]:
                    for j in range(final):
                        if values[i] > final[j]:
                            final[j] = uniques[i]
                else:
                    for j in range(final):
                        if values[i-1] > final[j]:
                            final[j] = uniques[i-1]
        return final

g = Solution()

nums = [1]
k = 1

print(g.topKFrequent(nums, k))

#compare dictionary values?






