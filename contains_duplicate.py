"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
def contains_duplicate(nums):
    """
    Checks if there are any duplicate numbers in the list.
    Args: nums (list): A list of integers.
    Returns: bool: True if any number appears more than once, False otherwise.
"""
    count={}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for element in count.keys():
        if count[element] > 1:
            return True
    return False

nums=[1,2,3,1]
print(contains_duplicate(nums))


def containsDuplicate(nums):
    a = set()
    for i in nums:
        if i in a:
            return True
        a.add(i)
    return False
nums=[1,2,3]
print(containsDuplicate(nums))