n=987
first = n
last = n%10

while(first>=10):
    first = first // 10

print("First Digit of {0} is {1}".format(n, first))
print("Last Digit of {0} is {1}".format(n, last))
