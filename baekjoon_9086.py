num = int(input())

for i in range(num):
    word  = input()
    if len(word) == 1:
        print(word+word)
    else:
        print(word[0]+word[-1])