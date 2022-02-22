a = 10 #float(input(" Please Enter the First Value a: "))
b = 20 #float(input(" Please Enter the Second Value b: "))

if(a > b):
    maximum = a
else:
    maximum = b

while(True):
    if(maximum % a == 0 and maximum % b == 0):
        print("\n Least Common Multiple of {0} and {1} = {2}".format(a, b, maximum))
        break;
    maximum = maximum + 1
