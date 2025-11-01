'''
Title: Two Sum

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

My Thought Process:
Since the problem is looking to get the sum of a number by adding two indices but also requires
you to not add the same indicies, you can simply use a nested for loop that iterates through
the list. i = 0 so that it starts at the first index, and j = 1 so that it starts at the 2nd
index and i should loop until nums-1 so that it won't reach the last index which would
prevent the same indices adding together


Time & space complexity:
O(n^2) time complexity
O(n) time complexity

'''
class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for i in range(len(nums)-1):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    result.append(i)
                    result.append(j)
                    return result
                j+=1
            i+=1

nums = [2,7,11,15]
target = 9

g = Solution()
print(g.twoSum(nums, target))


        
nums = [1, 2, 3, 4, 5]
target = 9


'''
Challenge:
Can you come up with an algorithm that is less than O(n^2) time complexity?



Time & space complexity:
O(n)

WHAT I LEARNED:
I learned how to use hashmaps and how you could create them dynamically 
through a loop. You can use a hashmap to find if a value(key) is in there
while only costing constant time. I learned that if I'm looking for a list
multiple times, I can simply just use a hashmap in order to not lose as much 
time searching. I simply have to find a way to get the value that I am looking 
for if not already determined.


'''


class OtherSolution(object):
    def twoSum(self, nums, target):
        my_dic = {}
        for i in range(len(nums)):
            my_dic[nums[i]] = i
            
        for i in range(len(nums)):
            current_target = target - nums[i]
            if current_target in my_dic:
                if my_dic[current_target] != i:
                    return i, my_dic[current_target]

h = OtherSolution()

print(h.twoSum(nums, target))





'''
My Thought Process:
This time the goal is to be able to find the nums for the target without making the hashmap 
beforehand(one pass). What can be done is to first check if the complement is in the hashmap
and return it's value which is the index along with the current index. If not in hashmap, then
simply add the current index to the hashmap. This was done so that you can prevent the same 
index to be returned if the complement is the same number as the current index. Inserting the 
currenth index to the hashmap first would make it so that you won't be able to check the previous
value in the hashmap because it will be overwritten by the current index.

What I learned:
same key overwrites the previous one with the same key name


'''


class BestSolution(object):
    def twoSum(self, nums, target):
        dic = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in dic:
                return [dic[complement], i]

            dic[nums[i]] = i

j = BestSolution()

print(j.twoSum(nums, target))