# import calendar module
import calendar

def calnderex():
    # ask of month and year
    year = int(input("Please Enter the year Number: "))
    month = int(input("Please Enter the month Number: "))

    # Displaying the Python calendar
    print(calendar.month(year, month))