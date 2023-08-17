'''Set: Remove Duplicates ( ** Interview Question)
You have been given a list my_list with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then prints the updated list.

You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a parameter and returns a new list with no duplicates.

Your function should not modify the original list, instead, it should create a new list with unique values and return it.

Example:



Input:
my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
 
Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]


Note:

The order of the elements in the updated list may be different from the original list, as sets are unordered.'''


def remove_duplicates(my_list):

    new_list = list(set(my_list))
    return new_list


def has_unique_char(string):
    
    char_set = set()

    for letter in string:
        if letter in char_set:
            return False
        char_set.add(letter)
    return True


def find_pairs(arr1,arr2,target):
    
    pairs = []
    for i in arr1:
        for j in arr2:
            if i + j == target:
                pairs.append((i,j))
                
    return list(pairs)

""" def find_pairs(arr1, arr2, target):
    set1 = set(arr1)
    pairs = []
    for num in arr2:
        complement = target - num
        if complement in set1:
            pairs.append((complement, num))
    return pairs """

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

print (find_pairs(arr1, arr2, target))


#print(has_unique_char('abacdef'))