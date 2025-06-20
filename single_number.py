"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
"""
def singleNumber(nums):
    """
       Finds the element that appears only once in a list where all other elements appear twice.

       Args: nums (list): A list of integers where every element appears twice except one.
       Returns: int: The element that appears only once.
       """
    count={}
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for element in count.keys():
        if count[element] == 1:
            return element
nums=[1,2,2]
print(singleNumber(nums))



def singleNumber1(nums):
    res = 0
    for i in nums:
        res ^= i
    return res
nums=[4,1,2,1,2]
print(singleNumber1(nums))