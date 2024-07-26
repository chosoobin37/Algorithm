num = input()
arr = [int(digit) for digit in num]

arr.sort(reverse=True)

new = 0
new = ''.join(map(str, arr))

print(new)