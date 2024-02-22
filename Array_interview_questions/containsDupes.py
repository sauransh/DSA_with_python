class Solution:
    def cont_dupes(self,nums:list[int])-> bool:
        dup = set(nums)
        if len(dup) == len(nums):
            return False
        else:
            return True
        

    # nums.sort()  # Sort the array in-place

    #     for i in range(1, len(nums)):
    #         if nums[i] == nums[i - 1]:
    #             return True

    #     return False

ss = Solution()

print(ss.cont_dupes([1,2,3,1]))