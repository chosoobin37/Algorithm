num = int(input())
words = []

for i in range(num):
    get = input()
    words.append(get)

# new_word = list(set(words))
# new_word.sort()
# new_word.sort(key = len)

words = list(set(words))
words.sort()
words.sort(key = len)

for i in words:
    print(i)