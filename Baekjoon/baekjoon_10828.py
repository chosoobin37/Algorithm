import sys
input = sys.stdin.readline

repeat = int(input().strip())
number = []

for i in range(repeat):
    order = input().strip().split()

    if order[0] == 'push':
        number.append(int((order[1])))
    elif order[0] == 'pop':
        if number:
            print(number.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(number))
    elif order[0] == 'empty':
        if number:
            print(0)
        else:
            print(1)
    elif order[0] == 'top':
        if number:
            print(number[-1])
        else:
            print(-1)