num = int(input())
members = []

for i in range(num):
    age, name = input().split()
    age = int(age)
    members.append((age, name, i))

def sort_members(member):
    return (member[0], member[2])

members.sort(key = sort_members)

for age, name, i in members:
    print(f"{age} {name}")