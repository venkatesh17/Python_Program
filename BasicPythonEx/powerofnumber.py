# Python Program to find Power of a Number

def powerofnumber():

    number = 3  # int(input(" Please Enter any Positive Integer : "))
    exponent = 4  # int(input(" Please Enter Exponent Value : "))
    power = 1

    for i in range(1, exponent + 1):
        power = power * number

    print("The Result of {0} Power {1} = {2}".format(number, exponent, power))