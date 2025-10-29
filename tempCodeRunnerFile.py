class Solution(object):
    def removeDuplicates(self, nums):
        i = len(nums)-1
        j = 0
        while j < len(nums)-1 and i != j:
            while nums[i] == nums[j] and i != j:
                nums.pop(j)
                i-=1
            j+=1
        k = len(nums)
        return k