count = 9
save= []

for i in range(count):
    num = int(input())
    save.append(num)

max_num=max(save)
max_index = save.index(max_num)

print(max_num)
print(max_index+1)