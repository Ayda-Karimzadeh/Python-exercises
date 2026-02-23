def is_leap(year):
    leap = False
    if 1900<year<100000:
        if (year%4 ==0 and year%100 !=0 ) or year%400==0 :
            leap = True
        else:
            leap = False
    else:
        pass
    return leap

year = int(input())
print(is_leap(year))