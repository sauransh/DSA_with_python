from collections import Counter
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        non_zero_index = 0

        # Move non-zero elements to the front
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
    
ss = Solution()
nums = [1,0,2,3,0]
ss.moveZeroes(nums)
print(nums)
        