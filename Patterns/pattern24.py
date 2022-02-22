
"""
    *
   * *
  * * *
 * * * *
* * * * *

    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

    A
   A B
  A B C
 A B C D
A B C D E
"""


def pattern24():
    n = 5
    for i in range(1, n+1):
        print(" "*(n-i), end="")
        for j in range(1, i+1):
            # print("*", end=" ")
            # print(j, end=" ")
            print(chr(64+j), end=" ")
        print()



