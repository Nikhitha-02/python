"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.
"""

def solution(a):
    """

    :param a: list:a list of elements
    :return: int: returns the minimum_difference
    """
    left=0
    total=sum(a)
    min_difference=None
    for i in range(1,len(a)):
        left+=a[i-1]
        right=total-left
        difference=abs(left-right)
        if min_difference is None or difference < min_difference :
            min_difference=difference
    return min_difference

testcase=[[-3,-1,-2,-4,3],
          [1,2,3,4,5,6,7],
          [8,7,5,4,6,3,2]]
for i in testcase:
    print(solution(i))

def solution1(a):
    a1=[]
    min_difference=[]
    temp=0
    for _ in range(len(a)-1):
        a1.append(a[temp])
        temp+=1
        left=sum(a1)
        a2=[]
        for j in range(len(a)-temp):
            a2.append(a[j+temp])
        right=sum(a2)
        difference=abs(left-right)
        min_difference.append(difference)
    return min(min_difference)

testcase=[[-3,-1,-2,-4,3],
          [1,2,3,4,5,6,7],
          [8,7,5,4,6,3,2]]
for i in testcase:
    print(solution1(i))

def solution2(a):
    """

    :param a: list:a list of elements
    :return: int: returns the minimum_difference
    """
    min_difference=None
    for i in range(1,len(a)):
        left=a[:i]
        right=a[i:]
        difference=abs(sum(left)-sum(right))
        if min_difference is None or difference < min_difference :
            min_difference=difference
    return min_difference

testcase=[[-3,-1,-2,-4,3],
          [1,2,3,4,5,6,7],
          [8,7,5,4,6,3,2]]
for i in testcase:
    print(solution2(i))