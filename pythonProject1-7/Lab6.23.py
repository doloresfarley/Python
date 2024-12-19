'''
6.23 LAB: Seasons

LAB ACTIVITY
6.23.1: LAB: Seasons


0 / 10

Write a program that takes a date as input and outputs the date's season in the northern hemisphere. The input is a string to represent the month and an int to represent the day.

Ex: If the input is:
'''
# List of months
# Dictionary with month as keys and maximum number of days as values
input_month = input()
input_day = int(input())
month_days = {
    "January": 31, "February": 29, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31,
    "September": 30, "October": 31, "November": 30, "December": 31
}


# Checking if month is valid
if input_month not in month_days:
    print("Invalid")
# Checking if the day is valid
elif input_day < 1 or input_day > month_days[input_month]:
    print("Invalid")

# Determine the season based on the date
elif (input_month == "March" and input_day >= 20) or (input_month in ["April", "May"]) or (input_month == "June" and input_day <= 20):
     print("Spring")
elif (input_month == "June" and input_day >= 21) or (input_month in ["July", "August"]) or (input_month == "September" and input_day <= 21):
    print("Summer")
elif (input_month == "September" and input_day >= 22) or (input_month in ["October", "November"]) or (input_month == "December" and input_day <= 20):
    print("Autumn")
elif (input_month == "December" and input_day >= 21) or (input_month in ["January", "February"]) or (input_month == "March" and input_day <= 19):
    print("Winter")