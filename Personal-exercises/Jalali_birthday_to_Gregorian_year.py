while True:

    def y(year,month,day):

        if 1<=month<=6 and 1<=day<=31:
           year=year+621
        elif 7<=month<=9 and 1<=day<=30:
            year=year+621
        elif month==10 and 1<=day<=10:
            year=year+621
        elif month==10 and 11<=day<=30 :
            year=year+621
        elif 11<=month<=12 and 1<=day<=29:
            year=year+622
        else:
            print("!")
        print(f"year of your birthday is {year}")

    day=int(input("enter day: "))
    month=int(input("enter month: "))
    year=int(input("enter year: "))
    y(year,month,day)