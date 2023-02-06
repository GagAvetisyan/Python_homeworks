# 85 ------------------------------------
# import math

# def getHypotenuse(a: float, b: float) -> float:
#     c = math.sqrt(a ** 2 + b ** 2)
#     return c
# print(getHypotenuse(4, 3))

# 86 ------------------------------------
# def getTotalFare(travelledRoad: int) -> float:
#     every140meter = travelledRoad / 140
#     fare = every140meter * 0.25
#     totalFare = 4 + fare
#     return totalFare
# print(getTotalFare(1400))

# 87 ------------------------------------
# def getTotalFee(numberItems: int) -> float:
#     if numberItems == 1:
#         return 10.95
#     elif numberItems > 1:
#         return 10.95 + (numberItems - 1) * 2.95
# print(getTotalFee(5)) 

# 88 ------------------------------------
# numbersList = []
# def getMedianValues(num1: int, num2: int, num3: int) -> float:
#     numbersList.append(num1)
#     numbersList.append(num2)
#     numbersList.append(num3)
#     return sum(numbersList) / len(numbersList)
# print(getMedianValues(3,4,6))

# 89 ------------------------------------
# def ordinalNumber():
#     number = int(input("Enter a number (1 - 12) "))
#     if number == 1:
#         return str(number) + "st"
#     elif number == 2:
#         return str(number) + "nd"
#     else:
#         return str(number) + "th"
# print(ordinalNumber())

# 91 ------------------------------------
# def ordinalDate(day: int, month: int, year: int) -> int:
#     daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     theNumberOfDay = 0
    
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         daysOfMonths[1] = 29
#     for i in range(month):
#         theNumberOfDay += daysOfMonths[i]
#     theNumberOfDay -= daysOfMonths[month] - day - 1

#     return theNumberOfDay
# print(ordinalDate(29,2,2004))

# 93 ------------------------------------
# def getCenterOfText(s: str, lineWidth: int) -> str:
#     emptySpace = lineWidth - len(s)
#     leftSpace = emptySpace // 2
#     return " " * leftSpace + s
# print(getCenterOfText("hello", 15))

# 94 ------------------------------------
# def myFunction(numbersList: list[float]) -> bool:
#     if numbersList[0] == 0 and numbersList[1] == 0 and numbersList[2] == 0:
#         return False
#     maxNumber = max(numbersList)
#     numbersList.remove(maxNumber)
#     if maxNumber > sum(numbersList):
#         return False
#     else:
#         return True
# print(myFunction([0,0,0]))

# 96 ------------------------------------
# def getStrToInt(string: str):
#     count = 0
#     for i in range(len(string)):
#         if string[i].isdigit() == True:
#             count += 1
#     if count == len(string):
#         print("It is integer")
#     else:
#         print("It is not integer")
# getStrToInt("5432")

# 97 ------------------------------------
# def precedence(operator: str) -> int:
#     if operator == "+" or operator == "-":
#         return 1
#     elif operator == "*" or operator == "/":
#         return 2
#     elif operator == "^":
#         return -1  
# operator = input("Enter an operator ")
# print(precedence(operator))

# 98 ------------------------------------
# def isPrime(number: int) -> bool:
#     if number == 1:
#         return False
#     elif number == 2:
#         return True
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#         return True
# print(isPrime(19))

# 99 ------------------------------------
# def isPrimeNumber(number: int) -> bool:
#     if number <= 1:
#         return False
#     elif number == 2:
#         return True
#     for i in range(2, int(number / 2 + 1)):
#         if number % i == 0:
#             return False
#     return True

# def nextPrimeNumber(number: int) -> int:
#     while True:
#         number += 1
#         if isPrimeNumber(number):
#             return number
# number = int(input("Enter a number "))
# print(nextPrimeNumber(number))
    
# 100 ------------------------------------
# import random

# def getRandomPassword():
#     newPassword = ""
#     for i in range(7, 11):
#         newPassword += chr(random.randint(36, 126))
#     return newPassword
# print(getRandomPassword())

# 101 ------------------------------------
# import random

# def getRandomPlate():
#     randomNumber = random.randint(0, 1)
#     randomPlate = ""
#     if randomNumber == 0:
#         for i in range(3):
#             randomPlate += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#         for i in range(3):
#             randomPlate += str(random.randint(0, 9))
#     else:
#         for i in range(4):
#             randomPlate += str(random.randint(0, 9))
#         for i in range(3):
#             randomPlate += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#     return randomPlate
# print(getRandomPlate())

# 102 ------------------------------------
# def checkPassword(password: str) -> str:
#     if len(password) < 8:
#         return False
#     lower = 0
#     upper = 0
#     digit = 0
    
#     for i in password:
#         if i.isupper():
#             upper += 1
#         elif i.islower():
#             lower += 1
#         elif i.isdigit():
#             digit += 1
#     if lower > 0 and upper > 0 and digit > 0:
#         print("Strong password")
#     else:
#         print("Bad password")   
# password = input("Enter password ")
# print(checkPassword(password))

# 106 ------------------------------------

# def daysCountInMonth(month: int, year: int) -> int:
#     daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         daysOfMonths[1] = 29
#     return daysOfMonths[month]

# month = int(input("Enter a month "))
# year = int(input("Enter a year "))
# print(daysCountInMonth(month, year))