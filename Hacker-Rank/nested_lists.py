if __name__ == '__main__':
    records=[]
    for _ in range(int(input())): #number of students
        name = input()
        score = float(input())
        records.append([name,score])
    #second lowest grade?
    #if we have several second lowest grade sort them alphabetically and print them
    scores=[]
    for j in records:
        scores.append(j[1])
    scores = sorted(set(scores))
    slow = scores[1]
    names=[]
    for i in records:
        if i[1]==slow:
            names.append(i[0]) 
    names.sort()
    for n in names:
        print(n)
    