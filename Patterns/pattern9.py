"""
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *
"""

def pattern9():
    n = 10
    for i in range(1, n):
        for j in range(1, i+1):
            print("*", end=" ")
        print()

    for i in range(1, n):
        print("* "*i)

