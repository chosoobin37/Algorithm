import sys
input = sys.stdin.readline

num = int(input())
students = []

for i in range(num):
    sn = input().strip()
    students.append(sn)

k = 1

while True:
    seen = set()
    for student in students:
        end = student[-k:]
        if end in seen:
            break
        seen.add(end)
    else:
        print(k)
        break

    k += 1   