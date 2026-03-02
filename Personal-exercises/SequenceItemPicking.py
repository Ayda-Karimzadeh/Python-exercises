letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
newlist = []
#list slicing is [start:end:step]
newlist=letters[0:11:2]

#OR newlist =letters[::2]
#OR for i in range(len(letters)):
#       if i%2==0 :
#           newlist.append(letters[i])
print(newlist)