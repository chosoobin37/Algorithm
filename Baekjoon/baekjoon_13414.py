import sys
input = sys.stdin.readline

k, l = map(int, input().split())   # k: 수강 가능 인원, l: 대기 목록 길이
dict = {}
for i in range(l):
    dict[input().strip()] = i

sorted_dict = sorted(dict.items(), key=lambda x: x[1])

for i in range(k):
    if i < len(sorted_dict):
        print(sorted_dict[i][0])
    else:
        break

# from collections import OrderedDict

# limit, click = map(int, input().split())
# wait = OrderedDict()

# for i in range(click):
#     sn = input().strip()
#     if sn in wait:
#         del wait[sn]
#     wait[sn] = None

# success = list(wait.keys())[:limit]

# for student in success:
#     print(student)

# limit, click = map(int, input().split())
# wait = []

# for i in range(click):
#     sn = input().strip()
#     if sn in wait:
#         wait.remove(sn)
#     wait.append(sn)

# success = wait[:limit]

# for student in success:
#     print(student)

# limit, click = map(int, input().split())
# wait = {}

# for i in range(click):
#     sn = input().strip()
#     if sn in wait:
#         del wait[sn]
#     wait[sn] = i

# success = sorted(wait.keys(), key=lambda x: wait[x])[:limit]

# for student in success:
#     print(student)