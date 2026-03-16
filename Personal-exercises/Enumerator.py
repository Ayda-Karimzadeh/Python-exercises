# a = [1, 2, 3]

# for i in a:
#     print(f"item {i} has index {i-1}")

a = [1, 2, 3]
for index, item in enumerate(a):
    print("Item %s has index %s" % (item, index))

# enumerate(a) creates an enumerate object which yields pairs of indexes and items.
# Then we iterate through that object print out the item-indexpairs in each iteration together with some other strings.