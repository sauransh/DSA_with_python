from collections import Counter
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        i = 0

        # Move non-zero elements to the front
        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
    
ss = Solution()
nums = [1,0,2,3,0]
ss.moveZeroes(nums)
print(nums)
        