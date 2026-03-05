# lista = []
# listb = []
# listc = []
# for i in range(1,11):
#     lista.append(i)
# for i in range(11,21):
#     listb.append(i)
# for i in range(21,31):
#     listc.append(i)
# d = dict(a = lista, b = listb, c = listc)
# print(d)

from pprint import pprint

d = {"a":list(range(1, 11)), "b":list(range(11, 21)), "c":list(range(21, 31))}
pprint(d)

# We're using ranges here to construct the lists. We're also using the built-in Python pprint  module, which is used to print out well-formatted views of datatypes in Python.