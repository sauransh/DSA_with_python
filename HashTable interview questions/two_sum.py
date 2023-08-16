'''HT: Two Sum ( ** Interview Question)
two_sum()

Problem:
Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.



Input:

A list of integers nums .

A target integer target.



Output:

A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].



Example:



Input: nums = [5, 1, 7, 2, 9, 3], target = 10
Output: [1, 4]
Explanation: The numbers at indices 1 and 4 in the array add up to the target 10.
 
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: The numbers at indices 1 and 2 in the array add up to the target 6.
 
Input: nums = [3, 3], target = 6
Output: [0, 1]
Explanation: The numbers at indices 0 and 1 in the array add up to the target 6.
 
Input: nums = [2, 1, 2, 7, 11, 15], target = 9
Output: [2, 3]
Explanation: Notice there are two 2s in the array.  The second one will be used.
 
Input: nums = [1, 2, 3, 4, 5], target = 10
Output: []
Explanation: There are no two numbers in the array add up to the target 10.
 
Input: nums = [], target = 0
Output: []
Explanation: There are no numbers in the input array, so the function returns an empty list [].'''


def two_sum(nums,target):
    num_map = {}

    for i,num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement],i]
        num_map[num] = i

print(two_sum([5,1,7,2,9],10))