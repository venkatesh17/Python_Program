
"""
A
A B
A B C
A B C D
A B C D E
A B C D E F
A B C D E F G
A B C D E F G H
"""
def pattern13():
    n = 10
    for i in range(1, n):
        for j in range(1, i):
            print(chr(64+j), end=" ")
        print()

