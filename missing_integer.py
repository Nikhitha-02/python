"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.
"""
def missing_integer(A):
    """

    :param A: list: a list of elements.
    :return: int: return the missing positive integer in a list.
    """
    A=set(A)
    i=1
    while i in A:
        i+=1
    return i

testcases=[[1, 3, 6, 4, 1, 2],[1, 2, 3],[-1,-3]]
for i in testcases:
    print(missing_integer(i))


















