"""
A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G
H H H H H H H H
I I I I I I I I I
J J J J J J J J J J
"""


def pattern12():
    n = 10
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chr(64+i), end=" ")
        print()

