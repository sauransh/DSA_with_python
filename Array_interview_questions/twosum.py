class Solution:
    def twosum(self, nums:list [int], target:int)-> list[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

ss= Solution()
nums = [2,7,11,15]
t = 9
print(ss.twosum(nums=nums,target=t))
