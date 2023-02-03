# 136 --------------------------------
# myDict = {
#     "a": 1,
#     "b": 2,
#     "c": 2,
#     "d": 4,
#     "e": 5,
#     "f": 1
# }

# value = int(input("Enter a value "))
# finalList = []

# for i in myDict:
#     if value == myDict[i]:
#         finalList.append(i)
# print(finalList)
# 138 --------------------------------
# myDict = {
#     ".": "1", ",": "11", "?": "111", "!": "1111", ":": "11111",
#     "A": "2", "B": "22", "C": "222",
#     "D": "3", "E": "33", "F": "333",
#     "G": "4", "H": "44", "I": "444",
#     "J": "5", "K": "55", "L": "555",
#     "M": "6", "N": "66", "O": "666",
#     "P": "7", "Q": "77", "R": "777", "S": "7777",
#     "T": "8", "U": "88", "V": "888",
#     "W": "9", "X": "99", "Y": "999", "Z": "9999",
#     " ": "0"
# }

# finalKeys = ""
# sentence = input("Enter words ").upper()

# for i in sentence:
#     if i in myDict:
#         finalKeys += myDict[i]
# print(finalKeys)
# 139 --------------------------------
# myDict = {
#     'a': '.-', 'b': '-...', 'c': '-.-.',
#     'd': '-..', 'e': '.', 'f': '..-.',
#     'g': '--.', 'h': '....', 'i': '..',
#     'j': '.---', 'k': '-.-', 'l': '.-..',
#     'm': '--', 'n': '-.', 'o': '---',
#     'p': '.--.', 'q': '--.-', 'r': '.-.',
#     's': '...', 't': '-', 'u': '..-',
#     'v': '...-', 'w': '.--', 'x': '-..-',
#     'y': '-.--', 'z': '--..',
#     '0': '-----', '1': '.----', '2': '..---',
#     '3': '...--', '4': '....-', '5': '.....',
#     '6': '-....', '7': '--...', '8': '---..',
#     '9': '----.'
# }

# finalCodes = ""
# sentence = input("Enter words ").lower()

# for i in sentence:
#     if i in myDict:
#         finalCodes += myDict[i] + " "
# print(finalCodes)
# 141 --------------------------------
# onesDict = {
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine"
# }

# tensDict = {
#     10: "ten",
#     11: "eleven",
#     12: "twelve",
#     13: "thirteen",
#     14: "fourteen",
#     15: "fifteen",
#     16: "sixteen",
#     17: "seventeen",
#     18: "eighteen",
#     19: "nineteen",
#     20: "twenty",
#     30: "thirty",
#     40: "forty",
#     50: "fifty",
#     60: "sixty",
#     70: "seventy",
#     80: "eighty",
#     90: "ninety"
# }

# number = int(input("Enter a number "))
# numberToWords = ""

# if number >= 100:
#     numberToWords += onesDict[number // 100] + " "
#     numberToWords += "hundred"
#     number %= 100
# if number in tensDict:
#     numberToWords += " " + tensDict[number]
# else:
#     numberToWords += " " + tensDict[number // 10 * 10]
#     if number % 10 != 0:
#         numberToWords += onesDict[number % 10]
# print(numberToWords)
# 142 --------------------------------
# string = input("Enter a word ")
# uniqeLetterCounts = {}

# for letter in string:
#     if letter in uniqeLetterCounts:
#         uniqeLetterCounts[letter] += 1
#     else:
#         uniqeLetterCounts[letter] = 1
# print(f"The number of unique characters is {len(uniqeLetterCounts)}")
# 143 --------------------------------
# string1 = input("Enter a word ").lower()
# string2 = input("Enter a word ").lower()
# count = 0

# for i in string1:
#     if i in string2:
#         count +=1
# if count == len(string1):
#     print(f"They are anagrams")
# else:
#     print(f"They are not anagrams")
# 144 --------------------------------
# words1 = input("Enter words ").lower().replace(" ", "")
# words2 = input("Enter words ").lower().replace(" ", "")
# count = 0

# for i in words1:
#     if i in words2:
#         count += 1
# if count == len(words2):
#     print(f"They are anagrams")
# else:
#     print("They are not anagrams")
# 145 --------------------------------
# scrabbleDict = {
#     'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }

# word = input("Enter a word ").upper()
# totalScore = 0

# for i in word:
#     totalScore += scrabbleDict[i]
# print(f"Total scrabble score is {totalScore}")
# 146 --------------------------------
# import random

# bingoDict = {
#     "B": [],
#     "I": [],
#     "N": [],
#     "G": [],
#     "O": [],
# }

# for i in bingoDict:
#     for _ in range(5):
#         if i == "B":
#             number = random.randint(1, 15)
#         elif i == "I":
#             number = random.randint(16, 30)
#         elif i == "N":
#             number = random.randint(31, 45)
#         elif i == "G":
#             number = random.randint(46, 60)
#         elif i == "O":
#             number = random.randint(61, 75)
#         bingoDict[i].append(number)
# print(bingoDict)

