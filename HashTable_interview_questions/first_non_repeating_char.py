'''HT: First Non-Repeating Character ( ** Interview Question)
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.'''


def first_non_repeating_char(string):
    char_count = {}

    for char in string:
        char_count[char] = char_count.get(char,0)+1

    for char in char_count:
        if char_count[char] == 1:
            return char
    return None

print(first_non_repeating_char('purple'))
print(first_non_repeating_char('aabbcc'))
print(first_non_repeating_char('hello'))