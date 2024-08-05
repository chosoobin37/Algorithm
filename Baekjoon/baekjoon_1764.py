seen, heard = map(int, input().split())
seen_heard = {}
count = 0

for i in range(seen):
    person = input().strip()
    seen_heard[person] = 1

for i in range(heard):
    person = input().strip()
    if person in seen_heard:
        seen_heard[person] += 1
        count += 1
    else:
        seen_heard[person] = 1

ppl = []

for person in seen_heard:
    if seen_heard[person] != 1:
        ppl.append(person)

ppl.sort()

print(count)
for person in ppl:
    print(person)

# seen, heard = map(int, input().split())
# seen_dict = {}
# heard_dict = {}

# for i in range(seen):
#     person = input().strip()
#     seen_dict[person] = True

# for i in range(heard):
#     person = input().strip()
#     heard_dict[person] = True

# result = sorted([person for person in seen_dict if person in heard_dict])

# print(len(result))
# for person in result:
#     print(person)

# seen, heard = map(int, input().split())
# seen_set = ()
# heard_set = ()

# for i in range(seen):
#     seen_set.add(input().split())

# for i in range(heard):
#     heard_set.add(input().split())

# result = sorted(seen_set & heard_set)

# print(len(result))
# for person in result:
#     print(person)