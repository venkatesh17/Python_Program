# If the sum of the digits of a given number raised to
# the power of its respective positions equals the actual number,
# it is a disarium number. For instance, 175 = 11 + 72 + 53 = 1 + 49 + 125 = 175.


Number = 175 # int(input("Enter the Number to Check Disarium Number = "))
length = len(str(Number))

Temp = Number
Sum = 0
rem = 0

while Temp > 0:
    rem = Temp % 10
    print("---rem--", rem)
    Sum = Sum + int(rem**length)
    Temp = Temp // 10
    length = length - 1

print("The Sum of the Digits = %d" %Sum)

if Sum == Number:
    print("\n%d is a Disarium Number." %Number)
else:
    print("%d is Not a Disarium Number." %Number)
