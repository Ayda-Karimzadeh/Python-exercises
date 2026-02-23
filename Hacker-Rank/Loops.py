if __name__ == '__main__':
    n = int(input())
    mylist = []
    if 1<=n<=20 :
        n=n-1
        for i in range(n,-1,-1):
            mylist.append(i*i)
            mylist.sort()
        for i in mylist:
            print(i)
            