# # ** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**

# # seq = ['soup','dog','salad','cat','great']
# # should be filtered down to:

# # ['soup','salad']

#filter object = filter() function is used to extract elements from an iterable (like a list, tuple or set) that satisfy a given condition. It works by applying a function to each element and keeping only those for which function returns True.

seq = ['soup','dog','salad','cat','great']

selected = filter(lambda x: x.startswith('s'), seq)
print(list(selected))

# selected = filter(lambda x: x[0] == 's', seq)
# print(list(selected))