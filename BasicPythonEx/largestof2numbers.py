

def largestof2numbers():
    # Python Program to find Largest of Two Numbers

    a = 10  # float(input(" Please Enter the First Value a: "))
    b = 8  # float(input(" Please Enter the Second Value b: "))

    if a > b:
        print("{0} is Greater than {1}".format(a, b))
    elif b > a:
        print("{0} is Greater than {1}".format(b, a))
    else:
        print("Both a and b are Equal")

