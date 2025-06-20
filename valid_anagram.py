"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""
def validAnagram(s,t):
    """
       Checks if two strings are anagrams of each other.

       Args:
       s (str): The first string.
       t (str): The second string.
       Returns: bool: True if s and t are anagrams (contain the same characters in any order), False otherwise.
    """
    return sorted(s) == sorted(t)
    # count={}
    # for char in s:
    #     if char in count:
    #         count[char] += 1
    #     else:
    #         count[char] = 1
    # for char in t:
    #     if char in count:
    #         count[char] -= 1
    # for char in count.values():
    #     if char != 0:
    #         return False
    # return True

print(validAnagram("anagram","nagaram"))