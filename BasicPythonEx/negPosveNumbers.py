
def negPosvenumbers():
    minimum = -14 # int(input("Enter the Minimum Number = "))
    maximum = 15 # int(input("Enter the Maximum Number = "))

    print("\nAll Negative Numbers from {0} and {1}".format(minimum, maximum))
    for num in range(minimum, maximum + 1):
        if num < 0:
            print(num, end='   ')

    print("\nAll Positive Numbers from {0} and {1}".format(minimum, maximum))
    for num in range(minimum, maximum + 1):
        if num > 0:
            print(num, end='   ')
