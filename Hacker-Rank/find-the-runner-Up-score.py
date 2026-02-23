#emtiaz nafar dovom?
if __name__ == '__main__':
    n = int(input()) #number of scores
    if 2<=n<=10:
        arr =list(map(int, input().split())) #scores
        start,end=-100,100
        in_range = all(start <= num <= end for num in arr)
        if in_range==True:
            arr.sort()
            arr = list(dict.fromkeys(arr))
            print(arr[-2])
        else:
            pass
    else:
        pass