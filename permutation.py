"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.
"""
def solution(A):
    """

    :param A: list:a list of elements
    :return: int: returns 1 if array A is a permutation and 0 if it is not.
    """
    sum=0
    n=len(A)
    for i in A:
        if A.count(i)<=1:
            sum+=i
    total_sum=n*(n+1)//2
    if total_sum==sum:
        return 1
    else:
        return 0

testcases=[[1,2,5],[33,34,36],[58,-56,57,59],[1,2,3],[1,1,4]]

for i in testcases:
    print(solution(i))
