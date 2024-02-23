'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
'''
# class Solution:
#     def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
#         for i in range(len(nums1)):
#             if nums1[i] not in nums2:
#                 print(nums1[i])
#                 nums1.pop(i)
                
#         return nums1
    
# ss= Solution()
# n1 = [4,9,5]
# n2 = [9,4,9,8,4]
# print(ss.intersect(n1,n2))

from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        # Count the occurrences of each element in both arrays
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        # Find the common elements and their minimum occurrences
        common_elements = counter1 & counter2

        # Build the result array based on common elements and their occurrences
        result = []
        for num, count in common_elements.items():
            result.extend([num] * count)

        return result

# Example usage:
ss = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
output = ss.intersect(nums1, nums2)
print(output)
