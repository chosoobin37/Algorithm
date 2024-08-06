# num = int(input())
# bag = 0

# if num % 5 == 0:
#     print(int(num/5))
# elif (num % 5)%3 == 0:
#     bag = int((num / 5)) + int((num % 5)/3)
#     print(bag)
# elif (num % 5) %3 != 0 and num %3 == 0:
#     print(int(num/3))
# else:
#     print(-1)

num = int(input())
bag = 0

while num >= 0:
    if num % 5 == 0:
        bag += int(num/5)
        print(bag)
        break
    num -= 3
    bag += 1
else: 
    print(-1)