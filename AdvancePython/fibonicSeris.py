# Fibinoic Series
# 0 1 1 2 3 5 8 13 21 34

from tkinter.constants import FIRST


i=0
First_Value = 0
Second_Value = 1

sum = 0

n=5

while(i <= n):    
    if i<=1:
        Next = i
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = Next
    
    print(Next)
    i=i+1
    
    
First = 0
Second = 1

for Num in range(0, n+1):
    sum = sum + First
    Next = First + Second
    First = Second
    Second = Next

    
    
print("=====" , sum)

        