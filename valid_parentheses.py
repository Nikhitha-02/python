"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
"""
def validParentheses(s):
    """
    Returns True if all brackets in the string are valid and balanced, else False.
    Args: s: A string containing brackets - (), [], {}
    Returns: True if the brackets are valid, otherwise False.
    """
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    if s == "":
        return True
    return False
print(validParentheses("()"))


