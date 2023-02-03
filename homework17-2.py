# 1 ----------------------------------
# myDict = {
#     "student1": 3,
#     "student2": 8,
#     "student3": 6,
#     "student4": 4,
#     "student5": 7,
#     "student6": 2,
#     "student7": 3,
#     "student8": 9,
#     "student9": 10,
#     "student10": 1
# }
# 2 ----------------------------------
# myDict = {
#     "student1": 3,
#     "student2": 8,
#     "student3": 6,
#     "student4": 4,
#     "student5": 7,
#     "student6": 2,
#     "student7": 3,
#     "student8": 9,
#     "student9": 10,
#     "student10": 1
# }

# sumRatings = 0

# for i in myDict:
#     sumRatings += myDict[i]

# ratingsAverage = sumRatings / len(myDict)
# print(ratingsAverage)
# 3 ----------------------------------
# myDict = {
#     "student1": 3,
#     "student2": 8,
#     "student3": 6,
#     "student4": 4,
#     "student5": 7,
#     "student6": 2,
#     "student7": 3,
#     "student8": 9,
#     "student9": 10,
#     "student10": 1
# }

# for i in myDict:
#     if myDict[i] < 5:
#         print("It is bad student")
#     else:
#         print("It is good student")
# 4 ----------------------------------
# myDict = {
#     "student1": 3,
#     "student2": 8,
#     "student3": 6,
#     "student4": 4,
#     "student5": 7,
#     "student6": 2,
#     "student7": 3,
#     "student8": 9,
#     "student9": 10,
#     "student10": 1
# }

# for i in myDict:
#     if myDict[i] >= 5:
#         print(f"{i} is good student")
# 5 ----------------------------------
# myDict = {
#     "student1": 3,
#     "student2": 8,
#     "student3": 6,
#     "student4": 4,
#     "student5": 7,
#     "student6": 2,
#     "student7": 3,
#     "student8": 9,
#     "student9": 10,
#     "student10": 1
# }

# for i in myDict:
#     if myDict[i] < 5:
#         print(f"{i} is bad student")
# 6 ----------------------------------
# myDict = {
#     "Paul": 3,
#     "Tom": 5,
#     "Jack": 7,
#     "Ann": 2
# }

# name = input("Enter a name ")

# if name in myDict:
#     print(f"Name: {name}, rating: {myDict[name]}")
# else:
#     print("Name is not in this dictionary")
# 7 ----------------------------------
# s = "a,2,b,5,c,8,a,4,e,11"
# newDict = {}
# s = s.split(",")
# print(s)

# for i in range(0, len(s), 2):
#     if s[i] in newDict:
#         newDict[s[i]] += int(s[i + 1])
#     else:
#         newDict[s[i]] = int(s[i + 1])
# print(newDict)
# 8 ----------------------------------
# word = "exercises"
# myLetters = {}

# for letter in word:
#     if letter in myLetters:
#         myLetters[letter] += 1
#     else:
#         myLetters[letter] = 1
# print(myLetters)
# 9 ----------------------------------
# oldList = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}] 

# newList = []

# for i in oldList:
#     if i not in newList:
#         newList.append(i)
# print(newList)
# 10 ----------------------------------
# questions = [
#     {
#         "question": "What is the country with the largest population?",
#         "options": ["USA", "India", "Great Britain", "Russia"],
#         "correctAnswer": "India"
#     }, 
#     {
#         "question": "What is the largest country in the world?",
#         "options": ["Russia", "China", "Great Britain", "Brasil"],
#         "correctAnswer": "Russia"
#     },
#     {
#         "question": "What is the capital of England?",
#         "options": ["Paris", "Praha", "London", "Madrid"],
#         "correctAnswer": "London"
#     }
# ]

# totalPrize = 0

# for question in questions:
#     print(question["question"])
#     for i in question["options"]:
#         print(question["options"])
#         break
#     answer = input("Enter the answer (1 - 4) ")
#     chosenAnswer = question["options"][int(answer) - 1]
#     if chosenAnswer == question["correctAnswer"]:
#             print("Correct")
#             totalPrize += 5000
#     else: 
#         print("incorrect")
#         break
# print(f"Your total prize is {totalPrize}")