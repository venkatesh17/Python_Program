# Python Program to find Student Grade
 
def StudentGrade():
    english = 89 #//float(input(" Please enter English Marks: "))
    math = 97 # float(input(" Please enter Math score: "))
    computers = 50 #float(input(" Please enter Computer Marks: "))
    physics = 78 #float(input(" Please enter Physics Marks: "))
    chemistry = 90 #float(input(" Please enter Chemistry Marks: "))

    total = english + math + computers + physics + chemistry
    percentage = (total / 500) * 100

    print("Total Marks = %.2f"  %total)
    print("Marks Percentage = %.2f"  %percentage)

    if(percentage >= 90):
        print("A Grade")
    elif(percentage >= 80):
        print("B Grade")
    elif(percentage >= 70):
        print("C Grade")
    elif(percentage >= 60):
        print("D Grade")
    elif(percentage >= 40):
        print("E Grade")
    else:
        print("Fail")