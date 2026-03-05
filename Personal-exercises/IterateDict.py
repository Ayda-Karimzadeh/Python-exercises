d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

# print(f"b has value {d['b']}")
# print(f"c has value {d['c']}")
# print(f"a has value {d['a']}")

for key, value in d.items():
    print(key, "has value", value)