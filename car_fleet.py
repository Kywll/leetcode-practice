'''
Problem name: Car Fleet

Link: https://leetcode.com/problems/car-fleet/description/

Description: 
There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.


My thought process:
The thought process was to first to store both positions and speed together then sort them.
This is done so that we could know the proper positions of them and be able to actually visualize
more easily and easily use a stack since it's sorted. To solve the problem, we simply had to get the
rate or the time it takes for each position to reach the end which is done by (target-position)/speed
then loop through the array and check if the current index is less than the previous one which we 
simply just skip through that loop and not append because that means it could catch up to the 
last index so therefor, it is a part of the fleet. If not then we simply just append the current
index which means it is a new fleet.

Time & space complexity:
O(nlogn) time - due to sorting
O(n) space

What I learned:
When using for each loop on a tuple we can simple just do for var1, var2 in tuple: instead of just 
using 1 variable for it so that it's more defined and easier to track.

'''

class Solution(object):
    def carFleet(self, target, position, speed):
        position_and_speed = []
        for i in range(len(position)):
            position_and_speed.append((position[i], speed[i]))
        
        position_and_speed = sorted(position_and_speed, reverse=True)

        stack = []

        print(position_and_speed)
        for c in position_and_speed:
            rate = (target - c[0]) / float(c[1])
            print(rate)
            if stack and rate <= stack[-1]:
                    continue
            stack.append(rate)

        return len(stack)
            
g = Solution()

target = 10
position = [6, 8]
speed = [3, 2]

print(g.carFleet(target, position, speed))



