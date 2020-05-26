"""
Problem:
  A programming contest organisation is planning a contest for several programmers, each of which has a certain rating. 
  (The higher the rating, the better the programmer.) Each programmer is paired with another programmer, and the difference between 
  their ratings is referred to as the "bias amount". Given the ratings of all the programmers in the contest, what is the minimum 
  total bias amount that can be achieved by optimally planning the programmer pairs?

  Example:
    n = 4 
    ratings = [4, 2, 5, 1]

    The optimal solution is:
    Pair the second programmer (2) with the fourth (1) for a difference of 1. Pair the first programmer (4) with the third (5) for a 
    difference of 1.
    This results in a total bias amount of 1 + 1 = 2.

  Function  Description:
    Complete the function minimizeBias in the editor below.

    minimizeBias has the following parameter:
      int ratings[n]: the ratings of each of the programmers
      Returns: 
        int: the minimum total bias amount that can be achieved in the contest

  Constraints:
    1 <= n <= 10^5
    1 <= ratings[i] <= 10^9
    n is even 



Solution:
"""

def minimizeBias(n, arr):
  arr.sort()
  res = 0
  for i in range(n-1, 0, -2):
    res += arr[i] - arr[i-1]
      
  return res

print(minimizeBias(4, [1, 3, 6, 6]))
print(minimizeBias(4, [4, 2, 5, 1]))