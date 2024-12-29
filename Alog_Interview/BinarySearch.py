
def BinarySearch(arr:list[int],low,high,k:int)-> int:
    if high>=low:
        mid = (high+low)//2
        if arr[mid]== k:
            return mid
        
        elif arr[mid]> k:
            return BinarySearch(arr,low,mid-1,k)
        
        else:
            return BinarySearch(arr,mid+1,high,k)
    else:
        return -1


def Binarysearch(arr:list[int], target:int):
    l,r= 0,len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            l = mid+1
        else:
            r= mid-1
    return -1


arr = [1,2,3,4,5,6,7,8,9]
k = 6
res = BinarySearch(arr=arr,low=0,high=len(arr)-1,k=k)
print(res)

res2 = Binarysearch(arr,k)
print(res2)