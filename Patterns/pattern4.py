"""
A A A A A A A A A A
B B B B B B B B B B
C C C C C C C C C C
D D D D D D D D D D
E E E E E E E E E E
F F F F F F F F F F
G G G G G G G G G G
H H H H H H H H H H
I I I I I I I I I I
J J J J J J J J J J
"""


def pattern4():
    n = 10
    for i in range(1, n):
        for j in range(1, n):
            print(chr(64+i), end=" ")
        print()


