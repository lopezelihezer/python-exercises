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
   
'''
n = 0
while n <= 100:
    print(n)
    n += 2

#  - Alter your loop to count backwards by 5's from 100 to -10.
n = 100
while n >= -10:
    print(n)
    n -= 5
#   - Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000.
n = 2
while n < 1000000:
    print(n)
    n = n*n 
# Write a loop that uses print to create the output shown below. 
n = 100
while n >= 5:
    print(n)
    n -= 5

# b. For Loops
#       i. Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number. 
x = 0
num = int(input("Give me a number and I'll show you the multiplication table for it. "))
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in num_list:
    while x < num * n:
        print(f"{num} x {n} = ", num*n)
        x = num*n
#       ii. Create a for loop that uses print to create the output shown below. 

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in num_list:
        print(f'{n}' * n)


# c. break and continue
    # i. Prompt the user for an odd number between 1 and 50. 
    # Use a loop and a break statement to continue prompting the user if they enter invalid input. 
    # (Hint: use the isdigit method on strings to determine this). 
    # Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.

num = str(input('Number to skip between 1 and 50: '))
if num.isdigit():
    continue
print('Bad Input!')
num = str(input('Please enter a number'))

for n in range(50):
    if n%2 == 0:
        continue
    print(f'Here is an odd number: {n}')



