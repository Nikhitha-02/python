"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

Write a function:

def solution(X, Y, D)

that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
"""
def solution(X, Y, D):
    """
     Parameters:
    X (int): The starting position of the frog.
    Y (int): The target position the frog.
    D (int): The fixed distance the frog covers in each jump.
    Returns:
    int: The minimal number of jumps required.
    """
    total_distance=Y-X
    jumps= total_distance // D
    if total_distance % D != 0:
        jumps+=1
    return jumps

print(solution(0,30,5))
print(solution(10, 85, 30))
print(solution(0, 10, 10))
print(solution(50, 50, 10))
print(solution(5, 6, 10))
print(solution(3, 17, 5))
print(solution(1, 1, 1))


