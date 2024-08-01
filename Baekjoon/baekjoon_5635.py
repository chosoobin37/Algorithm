num = int(input())
students = []

for i in range(num):
    name, d, m, y = input().split()
    d, m, y = int(d), int(m), int(y)
    students.append((y, m, d, name))

students.sort()

oldest = students[0][3]
youngest = students[-1][3]

print(youngest)
print(oldest)