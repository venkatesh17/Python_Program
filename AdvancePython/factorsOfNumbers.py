n=100

value = 1
print("Factors of Given Nunber {0} are :  ".format(n))

while(value <= n):
    if(n % value == 0):
        print("{0}".format(value))
    value+=1    
    