numbers =list(map(int, input().split(",")))
odd = 0
for num in numbers:
    if num%2!=0:
        odd += num    
print(odd)