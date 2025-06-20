"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""
a = "abcdmalayalamabcd"
p = ""

def is_polyndrome(b):
    """
    Checks if the given string is a palindrome.

    Args:b (str): The string to check.
    Returns:bool: True if the string is a palindrome, False otherwise.
    """
    return b == b[::-1]

r = []
i = 0

# Loop through each character in the string
while i < len(a):
    # Check from the end towards the current position
    for j in range(len(a) - 1, i, -1):
        # If matching characters found
        if a[i] == a[j]:
            # Check if the substring is a palindrome
            if is_polyndrome(a[i:j + 1]):
                print(a[i:j + 1])  # Print the palindrome
                r.append(len(a[i:j + 1]))  # Store its length
                i = j  # Skip to end of current palindrome
    i += 1



# def longest_palindromic_substring(s):
#     long= ""
#     for i in range(len(s)):
#         for j in range(i + 1, len(s) + 1):
#             substring = s[i:j]
#             if substring == substring[::-1] and len(substring) > len(long):
#                 long = substring
#     return long
# print(longest_palindromic_substring("babad"))