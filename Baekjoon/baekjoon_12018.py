sub, mil = map(int, input().split())
requirement  =[]

for i in range(sub):
    apply, limit = map(int, input().split())
    pay_mil = list(map(int, input().split()))

    if apply < limit:
        requirement.append(1)
    else:
        pay_mil.sort(reverse=True)
        requirement.append(pay_mil[limit-1])

requirement.sort()

count = 0
for req in requirement:
    if mil >= req:
        mil -= req
        count += 1
    else:
        break

print(count)

# sub, mil = map(int, input().split())
# count = 0

# for i in range(sub):
#     apply, limit = map(int, input().split())
#     pay_mil = list(map(int, input().split()))

#     pay_mil.sort(reverse = True) # 마일리지 높은순 정렬 (내림차순 정렬)

#     if apply < limit:
#         required_mil = 1
#     else:
#         required_mil = pay_mil[limit-1]

#     if mil >= required_mil:
#         mil -= required_mil
#         count += 1

# print(count)