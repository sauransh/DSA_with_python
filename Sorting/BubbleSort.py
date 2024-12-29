'''
bubble effect- last position fell in place i.e biggest element bubbling to position on right


nums = [-5,3,2,1,-3,-3,7,2,2]
start at position 1-> check if nums[i-1] > nums[i] => missplaced,swap operation
T: O(n^2)
S: O(1)
'''

def bubble(nums:list[int])->list[int]:

    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1], nums[j]
    return nums



nums = [-5,3,2,1,-3,-3,7,2,2]
print(bubble(nums))