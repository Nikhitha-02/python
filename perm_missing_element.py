"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.
"""
def solution(A):
    """

    :param A: list: a list of elements.
    :return: int: returns the missing element in the list.

    """
    sum=0
    n=len(A)+1
    for i in A:
        sum+=i
    total_sum=n*(n+1)//2
    return total_sum - sum
A=[1,2,3,5]
print(solution(A))


