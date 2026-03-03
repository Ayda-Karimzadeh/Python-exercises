a = ["1", 1, "1", 2]
print(list(set(a)))

#We used a set  function to convert the list to a set that would intermediately produce {'1', 1, 2}  with no duplicates because set objects cannot contain duplicates.

#If you need to preserve the order
# a = ["1", 1, "1", 2]
# a = list(dict.fromkeys(a))
# print(a)

# This is another solution that would preserve the original order
# The downside of this is that the operation can take a lot of time if the list as large as we need to access both lists and perform a conditional in each iteration.
# a = ["1", 1, "1", 2]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)