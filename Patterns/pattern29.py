"""
 ****
  ***
   **
    *

1111
 222
  33
   4

 55555
  4444
   333
    22
     1

"""


def pattern29():
    n = 5
    for i in range(1, n+1):
        # for j in range(1, n+1):
        # print(" "*(i-1), "*"*(n-i), end=" ")
        # print(" "*(i-1), str(i)*(n+1-i), end=" ")
        print(" "*(i-1), str(n+1-i)*(n+1-i), end=" ")
        print()

