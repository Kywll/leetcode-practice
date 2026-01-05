'''
Problem name: Time Based Key-Value Store

Link: https://leetcode.com/problems/time-based-key-value-store/description/

Description: 
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

My thought process:
The idea is to store value and timestamp pair in a list inside a dictionary. Then to get the values
you simply have to use a binary search based on the timestamps but only check if you can find the 
it, if not, then just use the previous one.

Time & space complexity:
O(log n) time
O(n) space

What I learned:
I learned that I could use binary search to find values on a specific side based on if I only want
smaller or larger elements than the target in case the target is not found.

'''

class TimeMap:
    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((value, timestamp))
        else:
            self.dic[key] = [(value, timestamp)]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        
        arr = self.dic[key]
        left = 0
        right = len(self.dic[key])-1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][1] <= timestamp:
                result = arr[mid][0]
                left = mid+1
            else:
                right = mid-1

        return result
    

obj = TimeMap()

obj.set("alice", "sad", 3)

print(obj.get("alice", 3))


