list1 =list(map(str,input().split(",")))
list2 =list(map(str,input().split(",")))
#list3 = list(zip(list1,list2))
#print(list3)
list3 = []
for i in range(len(list1)):
    list3.append((list2[i],list1[i]))
    i=i+1
print(list3)
