
def checkleapyear():
    # Check Leap Year using If Statement

    n = 2022  # 2000 int(input("Please Enter the Year Number you wish: "))

    for year in range(2000, n):
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            print("%d is a Leap Year" % year)
        else:
            print("%d is Not the Leap Year" % year)
