"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21
"""
def reverse_integer(n):
    """
        Reverses the digits of an integer.

        Args:n (int): The integer to reverse. Can be positive or negative.
        Returns:int: The reversed integer. Negative sign is preserved if input is negative.
        """
    reverse=0
    negative_number = n < 0
    n = abs(n)
    while n>0:
        digit = n % 10
        reverse = (reverse * 10) + digit
        n = n // 10
    return -reverse if negative_number else reverse

print(reverse_integer(-120))

