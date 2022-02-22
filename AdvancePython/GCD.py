num1 = 10 # float(input(" Please Enter the First : "))
num2 = 20 # float(input(" Please Enter the Second : "))

a = num1
b = num2

while(num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp

hcf = num1
print("\n HCF of {0} and {1} = {2}".format(a, b, hcf))


# Python Program to find GCD of Two Numbers

a = 20 #float(input(" Please Enter the First Value a: "))
b = 60 #float(input(" Please Enter the Second Value b: "))

i = 1
while(i <= a and i <= b):
    if(a % i == 0 and b % i == 0):
        val = i
    i = i + 1

print("\n HCF of {0} and {1} = {2}".format(a, b, val))



def findGreatestCD(a, b):
    if(b == 0):
        return a;
    else:
        return findGreatestCD(b, a % b)

num1 = 30
num2 = 50

Val = findGreatestCD(num1, num2)
print("\n GCD of {0} and {1} = {2}".format(num1, num2, Val))
