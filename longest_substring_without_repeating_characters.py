"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
def longest_substring_without_repeating_characters(s):
    """
    Finds the length of the longest substring without repeating characters.

    Args:s (str): Input string.
    Returns: int: Length of the longest substring with all unique characters.
    """
    temp = ""
    result = 0
    final = []
    for i in s:
        if i in temp:
            if len(temp) > result:
                result = len(temp)

            final.append(temp)
            temp = ""
        result = 0
        temp += i
    max_len = max([len(s) for s in final])
    return max_len

s = "aabcdabbcefghabcde"
print(longest_substring_without_repeating_characters(s))


# def longest_substring_without_repeating_characters(s):
#     """
#     Finds the length of the longest substring without repeating characters.
#
#     Args:
#     s (str): Input string.
#
#     Returns:
#     int: Length of the longest substring with all unique characters.
#     """
#     temp = ""
#     max_len = 0
#
#     for char in s:
#         if char in temp:
#             # Remove characters from the start until the duplicate is removed
#             temp = temp[temp.index(char)+1:]
#         temp += char
#         max_len = max(max_len, len(temp))
#
#     return max_len
#
# s = "aabcdabbcefghabcde"
# print(longest_substring_without_repeating_characters(s))
