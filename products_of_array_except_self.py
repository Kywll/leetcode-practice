'''
Problem name: Merge Sorted Array
Link: https://leetcode.com/problems/merge-sorted-array/description/?envType=problem-list-v2&envId=array
Description:

My thought process:

Time & space complexity:
O(n^2) time
O(1) space ignoring output array

'''

class Solution(object):
    def productExceptSelf(self, nums):
        result = []
        for i in range(len(nums)):
            products = 1
            for j in range(len(nums)):
                if j != i:
                    products *= nums[j]
            result.append(products)
        return result

g = Solution()


nums = [1,2,3,4]
print(g.productExceptSelf(nums))



'''
Thought Process:
The idea is to count how many zeroes there are and count the total product while excluding zeroes
since it would result to 0 if included. The next step is to check if the zero count is greater 
than 1, which means that every product except self will result to a 0, so you simply just keep
appending zeroes. Else, you check if it's only 1, which means that the index with a 0 will 
contain the total product because the one and only zero which is the index will not be included
in the products and everything else will be 0 because at that point, the total product will
keep getting multiplied by 0. And lastly, if there are no zeroes at all, then you can simply 
get the value of products of array except self by simply just dividing by the index itself. 

Time & space complexity:
O(n) time
O(1) space ignoring output array
'''


class Solution(object):
    def productExceptSelf(self, nums):
        total_products = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_products *= num
        result = []
        for num in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                if num == 0:
                    result.append(total_products)
                else:
                    result.append(0)
            else:
                result.append(total_products // num)
        return result

g = Solution()


nums = [0,1,2,3,4]
print(g.productExceptSelf(nums))

'''
Thought Process:
The idea was to calculate the prducts of each numbers before the current index and also calculate
the product of all numbers after the current index then multiply them together after you calculated
them. This is also stored so that you first store products of previous numbers one by one and 
multiplying it again to the previous result or products. This is done so that we can choose until
what product before or after the current index is in. These arrays are filled by multiplying each 
new element with the result previously computed, so each step reuses earlier results.

Time & space complexity:
O(n) time
O(n) space
'''


class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [nums[0]] * n
        postfix = [nums[len(nums)-1]] * n

        for i in range(1, len(nums)):
            prefix[i] = (prefix[i-1] * nums[i])
        
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = (postfix[i+1] * nums[i])
        
        result = [postfix[1]]
        i = 0
        j = 2
        while i < len(nums)-2:
            result.append(prefix[i] * postfix[j])
            i+=1
            j+=1
        
        result.append(prefix[i])
        return result
        
g = Solution()


nums = [1,2,3,4]
print(g.productExceptSelf(nums))



