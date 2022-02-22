"""
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
A B C D E F G H I J
"""


def pattern5():
    v = 10
    for i in range(1, v):
        for j in range(1, v):
            print(chr(64+j), end=" ")
        print()