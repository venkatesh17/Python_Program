"""
J J J J J J J J J
I I I I I I I I I I
H H H H H H H H H H
G G G G G G G G G G
F F F F F F F F F F
E E E E E E E E E E
D D D D D D D D D D
C C C C C C C C C C
B B B B B B B B B B
A A A A A A A A A A
"""


def pattern7():
    n = 10
    for i in range(1, n):
        for j in range(1, n):
            print(chr(65+n-j), end=" ")   # print(chr(65+n-i), end=" ")
        print()
