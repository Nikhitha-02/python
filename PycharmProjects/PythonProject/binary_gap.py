"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

Write a function:

def solution(N)

that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
"""
def binary_number(n):
    """

    :param n: int: positive integer.
    :return: int: returns the length of the zeros between the 1's in a given number.
    """
    binary_n = binary(n)
    max_gap = 0
    current_gap = 0
    for bit in binary_n:
        if bit == '1':
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        else:
            current_gap += 1

    return max_gap

def binary(n):
    # did not use the binary() type coneversion to convert the given number into binary number.
    if n==0:
        return 0
    binary=""
    while n>0:
        binary=str(n % 2 )+binary
        n=n//2
    return binary
print(binary_number(9))

import re
#using the regular expressions.
def gap(n):
    binary_number = bin(n)[2:]
    binary_gap = re.findall(r'(?<=1)0+(?=1)', binary_number)
    return max(map(len, binary_gap),default=0)

print(gap(9))

def binary_number(n):
    #usinggit push -u origin main the split method.
    n= bin(n)[2:]
    binary_gap =n.strip('0').split('1')[1:]
    return max(map(len, binary_gap), default=0)
print(binary_number(32))