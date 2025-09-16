// to check wether given year is leap year or not , since we r using return type bool if it says true then is leap year , if says false  then it is not leap year.
    //// passed all cases
year = int(input())
print(is_leap(year))

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)



////////////// passed 4 out of six cases
def is_leap(year):
    x= year % 4 
    y =  year % 100
    if x == 0 and y != 0 :
        return True
    else:
        return False

year = int(input())
print(is_leap(year))
