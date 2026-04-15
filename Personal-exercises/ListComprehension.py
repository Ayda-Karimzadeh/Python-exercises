names = ["amir","milad","hossein","reza","mehdi"]

# newlist = []
# for name in names:
#     if "a" in name:
#         newlist.append(name)
#
# print(newlist)

# newlist = [name for name in names if "a" in name]
# print(newlist)

# newlist = [name.upper() for name in names if "a" in name]
# print(newlist)

newlist = [name if name != "amir" else "jafar" for name in names]
print(newlist)

# numbers = [1,2,3,4,5]
# newlist = [number *2 for number in numbers]
# print(newlist)

