# 1 ------------------------------------
# myDict = {
#     "a": 3,
#     "b": 2,
#     "c": 7,
#     "d": 1
# }

# sortedDict = {}

# sortedKeys = sorted(myDict, key = myDict.get)
# print(sortedKeys)

# for i in sortedKeys:
#     sortedDict[i] = myDict[i]

# print(sortedDict)
# 2 ------------------------------------
# myDict = {
#     "a": 3,
#     "b": 2,
#     "c": 7,
#     "d": 1
# }

# myDict["e"] = 10
# print(myDict)
# 3 ------------------------------------
# myDict = {
#     "a": 3,
#     "b": 2,
#     "c": 7,
#     "d": 1
# }

# if "d" in myDict:
#     print("Yes, there is")
# else:
#     print("There is not")
# 4 ------------------------------------
# dict1 = {"a": 50, "b": 700}
# dict2 = {"c": 400, "d": 600}

# dict1.update(dict2)
# print(dict1)
# 5 ------------------------------------
# sum = 0
# myDict = {"a": 1, "b": 2, "c": 12}

# for i in myDict:
#     sum += myDict[i]
# print(sum)
# 6 ------------------------------------
# myDict = {
#     "D": 56,
#     "E": 12,
#     "F": 69,
#     "C": 45,
#     "B": 23,
#     "A": 67
# }

# maxValues = {}
# count = 0

# sortedKey = sorted(myDict, key = myDict.get, reverse = True)

# for i in sortedKey:
#     if count != 3:
#         maxValues[i] = myDict[i]
#         count += 1
#     else:
#         break
# print(maxValues)