'''
selection sort: find min index, and swap with position of i 
         <-j
           i->
nums = [-5,3,2,1,-3,-3,7,2,2]
start at position 0
T: O(n^2)
S: O(1)
'''

def selection_sort(nums:list[int])->list[int]:

    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums

nums = [-5,3,2,1,-3,-3,7,2,2]
print(selection_sort(nums))