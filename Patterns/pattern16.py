"""
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""


def pattern16():
    n = 10
    for i in range(1, n+1):
        for j in range(1, n+2-i):
            print(j, end=" ")
        print()
