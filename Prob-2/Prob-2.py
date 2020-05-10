# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Caleb Howard

'''
Input: Asks user for name, hourly wage, and how many hours they worked this week.
Process: Calculates the users regular wages, overtime wages, total wages, tax withholding amount, insurance withholding amount, and take home pay.
Output: Print out a paycheck statement with the users name, regular wage amount, overtime wage amount, total wage amount, tax withholding amount, insurance withholding amount, and take home pay.
'''

def main():
    print("Hello, what is your name?")
    userName = input()
    print("What is your hourly wage?")
    hourlyWage = int(input())
    print("How many hours have you worked this week?")
    employeeHours = int(input())

    # calculating wages, tax withholding, insurance withholding, and take home pay
   
    if employeeHours > 40:
        overtimeWage = (employeeHours - 40)*hourlyWage*1.5
    else:
        overtimeWage = 0
    
   
    regularWage = hourlyWage*employeeHours
    
    totalWage = regularWage + overtimeWage

    taxWithhold = totalWage*.20
    insuranceWithhold = totalWage*.10

    takehomePay = totalWage - taxWithhold - insuranceWithhold

    # paycheck form

    print("Here is your paycheck:")
    print(userName)
    print("Regular wage:", regularWage)
    print("Overtime wage:", overtimeWage)
    print("Tax withhold:", taxWithhold)
    print("Insurance withhold:", insuranceWithhold)
    print("Take home pay:", takehomePay)


main()