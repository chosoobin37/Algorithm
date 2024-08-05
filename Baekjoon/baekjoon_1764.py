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
