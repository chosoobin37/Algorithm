from collections import deque
import sys
input = sys.stdin.readline

repeat = int(input())
number = deque()

for i in range(repeat):
    order = input().strip().split()

    if order[0] == '1':
        number.appendleft(int(order[1]))
    elif order[0] == '2':
        number.append(int(order[1]))
    elif order[0] =='3':
        print(number.popleft() if number else -1)
    elif order[0] == '4':
        print(number.pop() if number else -1)
    elif order[0] == '5':
        print(len(number))
    elif order[0] == '6':
        print(0 if number else 1)
    elif order[0] == '7':
        print(number[0] if number else -1)
    elif order[0] == '8':
        print(number[-1] if number else -1)

