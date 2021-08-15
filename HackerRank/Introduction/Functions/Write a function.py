def is_leap(year):
    leap = True
    
    return (year%4==0) and (year%400 == 0 or year%100!=0)

year = int(raw_input())

