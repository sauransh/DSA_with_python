'''
Find the largest/smallest element in an array.
'''

def FindElement(nums:list[int])-> int:
    largest = float('-inf')
    smallest = float('inf')

    for n in nums:
        if n > largest:
            largest = max(largest,n)
        
        if n < smallest:
            smallest = min(smallest,n)
    
    return largest,smallest

array = [3, 5, 1, 9, 7, -2, 0]
largest, smallest = FindElement(array)
print(f"Largest: {largest}, Smallest: {smallest}")