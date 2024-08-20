from collections import deque
import sys
input = sys.stdin.readline

repeat = int(input())
number = deque()

for i in range(repeat):
    order = input().strip().split()

    if order[0] == 'push_front':
        number.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        number.append(int(order[1]))
    elif order[0] == 'pop_front':
        if number:
            print(number.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
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
    elif order[0] == 'front':
        if number:
            print(number[0])
        else:
            print(-1)
    elif order[0] == 'back':
        if number:
            print(number[-1])
        else:
            print(-1)
    
