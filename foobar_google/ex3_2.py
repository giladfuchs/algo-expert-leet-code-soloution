'''
The Grandest Staircase Of Them All
==================================
With the LAMBCHOP doomsday device finished, Commander Lambda is preparing to debut on the galactic stage -- but in order to make a grand entrance, Lambda needs a grand staircase! As the Commander's personal assistant, you've been tasked with figuring out how to build the best staircase EVER.

Lambda has given you an overview of the types of bricks available, plus a budget. You can buy different amounts of the different types of bricks (for example, 3 little pink bricks, or 5 blue lace bricks). Commander Lambda wants to know how many different types of staircases can be built with each amount of bricks, so they can pick the one with the most options.

Each type of staircase should consist of 2 or more steps. No two steps are allowed to be at the same height - each step must be lower than the previous one. All steps must contain at least one brick. A step's height is classified as the total amount of bricks that make up that step.
For example, when N = 3, you have only 1 choice of how to build the staircase, with the first step having a height of 2 and the second step having a height of 1: (# indicates a brick)

#
##
21

When N = 4, you still only have 1 staircase choice:

#
#
##
31

But when N = 5, there are two ways you can build a staircase from the given bricks. The two staircases can have heights (4, 1) or (3, 2), as shown below:

#
#
#
##
41

#
##
##
32

Write a function called solution(n) that takes a positive integer n and returns the number of different staircases that can be built from exactly n bricks. n will always be at least 3 (so you can have a staircase at all), but no more than 200, because Commander Lambda's not made of money!

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution(200)
Output:
    487067745
4-3-1
5-2
321,42,51-6  -3
421,43,52,61, -7-4
521,431,53,62,71  -8-5
621,531,432,81,72,63,54 - 9 -7
721,631,541,532,4321,91,82,73,64-10-9
821,731,641,5321,542,632,92,83,74,65 - 11-10
'''


def solution(n):
    mat = [[0 for _ in range(n+1)] for _ in range(n+1)]

    mat[0][0] = 1
    for i in range(1, n+1):
        for j in range(n+1):
            mat[i][j] = mat[i-1][j]
            if j >= i:
                mat[i][j] += mat[i-1][j-i]
    return mat[n][n] - 1


print(solution(10))
