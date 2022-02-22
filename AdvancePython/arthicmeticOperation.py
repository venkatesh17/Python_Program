def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def floordivision(num1, num2):
    return num1 // num2

def modulus(num1, num2):
    return num1 % num2

def exponent(num1, num2):
    return num1 ** num2

num1 = 10 #int(input("Enter the First Value  = "))
num2 = 2 #int(input("Enter the Second Value = "))

print("The Addition       = {0}".format(addition(num1, num2)))
print("The Subtraction    = {0}".format(subtraction(num1, num2)))
print("The Multiplication = {0}".format(multiplication(num1, num2)))
print("The Division       = {0}".format(division(num1, num2)))
print("The Floor Division = {0}".format(floordivision(num1, num2)))
print("The Modulus        = {0}".format(modulus(num1, num2)))
print("The Exponent       = {0}".format(exponent(num1, num2)))