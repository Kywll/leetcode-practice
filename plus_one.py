'''
Problem name: Plus One
Link: https://leetcode.com/problems/plus-one/description/?envType=problem-list-v2&envId=array
Description:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

My thought process:
The first thing I did was to make a way to return the result if the digits end was not 9 which is
done by simply just adding 1 to it. The next part is to find a way to determine what happens when
the end is 9. What I did is first add 1 to the last number, and check if it is more than 10 or 
not. This is done in order to check cases where the end is 9 but the start is less than 9 like 
[8,9]. Simply changing 9 to 1 and appending 0 will not work since it is meant to be treated as
an actual number. At that point you simply just return it because you no longer have to it to 1
and 0 compared to 9. In the case that it is 10, you turn it into 0 then reduce the index in 
order to acces the index before. Now if there is still an index, it will still loop and if it's
less then 10, then it just adds one to it then returns it. But if it's 10 and the you're already
past the index, then that means it's all 9, that means you have to make the first index into 1
then append 0 into the end.

Time & space complexity:
O(n) time
O(1) space

'''


class Solution(object):
    def plusOne(self, digits):
        if digits[len(digits)-1] == 9:
            i = len(digits)-1
            while i >= 0:
                digits[i] +=1
                print(digits[i])
                if digits[i] < 10:
                    return digits
                else:
                    digits[i] = 0
                    i-=1
            digits[i+1] = 1
            digits.append(0)
            return digits
                    
        digits[len(digits)-1] +=1
        return digits
        

digits = [1,2,3]
g = Solution()

print(g.plusOne(digits))







