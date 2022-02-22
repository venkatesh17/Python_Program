"""
I H G F E D C B A
I H G F E D C B A
I H G F E D C B A
I H G F E D C B A
I H G F E D C B A
I H G F E D C B A
I H G F E D C B A
I H G F E D C B A
I H G F E D C B A
"""


def pattern8():
    n = 10
    for i in range(1, 10):
        for j in range(1, 10):
            print(chr(65+n-j-1), end=" ")
        print()
