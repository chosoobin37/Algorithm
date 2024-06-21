hour, min=map(int, input().split())

if hour != 0:
    if min >= 45:
        print (hour, (min-45))
    elif min < 45:
        print((hour-1), ((min-45)+60)) 
elif hour == 0:
    if min >= 45:
        print("0", (min-45))
    elif min < 45:
        print("23", ((min-45)+60))