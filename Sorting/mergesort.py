'''
nums = [-5,3,2,1,-3,-3,7,2,2]
T: O(nlog(n))
S: O(n)/ harder : O(log(n))
'''


def merge_sort(arr:list[int])->list[int]:
    n = len(arr)

    if n == 1:
        return arr
    
    mid = n //2
    L = arr[:mid]
    R = arr[mid:]
    
    L = merge_sort(L)
    R = merge_sort(R)

    l,r = 0,0
    L_len = len(L)
    R_len = len(R)

    sorted_arr = [0]*n
    i = 0

    while l < L_len and r < R_len:

        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l+=1
        else:
            sorted_arr[i] = R[r]
            r+=1
        i+=1
    
    while l < L_len:
        sorted_arr[i] = L[l]
        l+=1
        i+=1
    
    while r < R_len:
        sorted_arr[i] = R[r]
        r+=1
        i+=1
    
    return sorted_arr

nums = [-5,3,2,1,-3,-3,7,2,2]
print(merge_sort(nums))


def quick_sort(arr):
    
    if len(arr) <=1:
        return arr
    
    pivot = arr[-1]

    L = [x for x in arr[:-1] if x<= pivot]
    R = [x for x in arr[:-1] if x> pivot]
    
    L = quick_sort(L)
    R = quick_sort(R)

    return L + [pivot] + R

print(quick_sort(nums))