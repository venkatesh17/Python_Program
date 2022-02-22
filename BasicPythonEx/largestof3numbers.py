
def largest3number():
    # Python Program to find Largest of Three Numbers using Elif Statement

    a = 12  # float(input("Please Enter the First value: "))
    b = 6 # float(input("Please Enter the First value: "))
    c = 8 # float(input("Please Enter the First value: "))

    if a > b and a > c:
        print("{0} is Greater Than both {1} and {2}".format(a, b, c))
    elif b > a and b > c:
        print("{0} is Greater Than both {1} and {2}".format(b, a, c))
    elif c > a and c > b:
        print("{0} is Greater Than both {1} and {2}".format(c, a, b))
    else:
        print("Either any two values or all the three values are equal")
