'''
Problem name: Number of Employees Who Met the Target
Link: https://leetcode.com/problems/number-of-employees-who-met-the-target/description/?envType=problem-list-v2&envId=array
Description:
There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.
The company requires each employee to work for at least target hours.
You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.
Return the integer denoting the number of employees who worked at least target hours.

My thought process:
Just loop through the array and check if the current index is equals to the target or grater

Time & space complexity:
O(n) time
O(1) space
'''

class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        result = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                result += 1
        return result
    
hours = [0,1,2,3,4]
target = 2