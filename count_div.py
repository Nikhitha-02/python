"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.
"""
def count_div(A,B,K):
    """

    :param A: int: starting number of the range.
    :param B: int: last number of the range.
    :param K: int: the number to divisible by.
    :return: int: returns the no.of integers in the range[A,B] that are divisible by K.
    """
    count=0
    for i in range(A,B+1):
        if i%K==0:
            count+=1
    return count

A=6
B=11
K=2
print(count_div(A,B,K))
