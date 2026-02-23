while True:
    def mynum(num):
        if num%2==0:
            print("number is even!")
        elif num%2==1:
            print("number is odd!")
        else:
            pass
    num = int(input("enter number: "))
    mynum(num)