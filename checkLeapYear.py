# A leap year is exactly divisible by y except for century years (years ending with 00).
# The century year is a leap year only if it is perfectly divisible by 400 for eg:-

# 2017 is not a leap year
# 1900 is not a leap year
# 2012 is a leap year
# 200 is a leap year

year = 2004

if(year % 4) == 0:
    if(year % 100 ) ==0:
        if(year % 400) ==0:
            print(year, "is a leap year")
        else:
            print(year, "is not a a leap year")
    else:
        print(year, "is a leap year")
else:
    print(year, "is not a leap year")