
def pattern14():
    n = 5
    for i in range(1, n+1):
        for j in range(1, n+2-i):
            print("* ", end=" ")
        print()

