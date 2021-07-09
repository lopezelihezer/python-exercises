# Control Structures Exercises

# Conditional Basics
# a. prompt the user for a day of the weekm print out whether the day is Monday or not. 
x = input('What day of the week is it?')
if x == "Monday":
    print(f"You're correct, today is {x}")
else:
    print(f"Today is not {x}")

# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend
weekday = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['saturday', 'sunday', 'Saturday', 'Sunday']
x = input('What day of the week is it?')
if x in weekday:
    print(f"Today is a weekday")
else: 
    print("Today is a weekend")
# c. Create variables and make up values for:
# the number of hours worked in a week
# the hourly rate
# how much the week's paycheck will be

hrs_worked = 40
hr_rate = 50
weekly_paycheck = hrs_worked * hr_rate

'''
2. Loop Basics
    a. While
        - Create an integer variable i iwth a value of 5
        - Create a while loop that runs so long as i is less than or equal to 15
        - Each loop iteration, output the current value of i, then increment i by one.

'''
i = 5
while i <= 15:
    print(i)
    i += 1

'''
    - Create a while loop that will count by 2's starting with 0 and ending at 100.
    Follow each number with a new line.
    - Alter your loop to count backwards by 5's from 100 to -10.
    - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.
'''
n = 0
while n <= 100:
    print(n)
    n += 2
