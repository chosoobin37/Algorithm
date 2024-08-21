import sys
input = sys.stdin.read
data = input().splitlines()

repeat = int(data[0])
number = []

for i in range(1, repeat+1):
    order = data[i].split()

    if order[0] == '1':
        number.append(int(order[1]))
    elif order[0] == '2':
        if number:
            print(number.pop())
        else:
            print(-1)
    elif order[0] == '3':
        print(len(number))
    elif order[0] == '4':
        print(0 if number else 1)
    elif order[0] == '5':
        if number:
            print(number[-1])
        else:
            print(-1)

# import sys
# input = sys.stdin.read

# repeat = int(input().strip())
# number = []

# for i in range(repeat):
#     order = input().strip().split()

#     if order[0] == 1:
#         number.append(int(order[1]))
#     elif order[0] == 2:
#         if number:
#             print(number[0])
#         else:
#             print(-1)
#     elif order[0] == 3:
#         print(len(number))
#     elif order[0] == 4:
#         print(0 if number else 1)
#     elif order[0] ==5:
#         print(number[0] if number else -1)