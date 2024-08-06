num = int(input())
count = 0
current = set()

for i in range(num):
    content = input().strip()
    if content == "ENTER":
        current.clear()
    elif content not in current:
        current.add(content)
        count += 1

print(count)