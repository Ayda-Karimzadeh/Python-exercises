while True:
    def myfunc(name):
        countL=0
        countC=0
        for i in name:
            if 96<ord(i)<123:
                countL=countL+1
            elif 64<ord(i)<91:
                countC=countC+1
            else:
                pass

        print(f"Upper cases: {countC}")
        print(f"Lower cases: {countL}")
    name = input("enter name: ")
    myfunc(name)