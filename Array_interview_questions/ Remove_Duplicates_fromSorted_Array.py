''''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
'''

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        i = 0

        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
        print(nums[:i+1])
        return i+1

# Different approach
        # d = set()
        # for i in range(len(nums)):
        #     d.add(nums[i])
        # return len(d)

# Different approach
        # d= set(nums)
        # return len(d)

ss = Solution()

nums = [0,0,1,1,1,2,2,3,3,4]
print(ss.removeDuplicates(nums))