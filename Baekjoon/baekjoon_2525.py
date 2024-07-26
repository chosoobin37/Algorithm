hour, min=map(int, input().split())
time = int(input())

if min+time<60:
    print(hour, min+time)
elif min+time>=60:
    if int(hour+(min+time)/60) == 24: 
        print(0,(min+time)%60)
    elif int(hour+(min+time)/60) > 24:
        print(int(hour+(min+time)/60)-24,(min+time)%60)
    else: 
        print(int(hour+(min+time)/60), (min+time)%60)