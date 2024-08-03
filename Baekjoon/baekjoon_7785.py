num = int(input())
records= set()  # 시간복잡도 고려

for i in range(num):
    name, log = input().split()

    if log == 'enter':
        records.add(name)
    elif log == 'leave':
        if name in records:
            records.discard(name)

sorted_records = sorted(records, reverse = True)

for name in sorted_records:
    print(name)