"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6
7 7 7 7 7 7 7
8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9
10 10 10 10 10 10 10 10 10 10
"""
def pattern10():
    n = 10
    for i in range(1, n+1):
        for j in range(0, i):
            print(i, end=" ")
        print()

