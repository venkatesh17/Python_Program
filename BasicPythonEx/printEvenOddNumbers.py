
def evenoddnumbers():
    # Python Program to Print Even Numbers from 1 to N

    maximum = 20  # int(input(" Please Enter the Maximum Value : "))

    print("Even Numbers")
    for number in range(1, maximum + 1):
        if number % 2 == 0:
            print("{0}".format(number), end=" ")

    print()
    print("Odd Numbers")
    for number in range(1, maximum + 1):
        if number % 2 != 0:
            print("{0}".format(number), end=" ")
