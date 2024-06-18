word = input().strip().upper()

freq = [0] * 26
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for char in word:
    index = alphabet.index(char)
    freq[index] += 1

max_freq = max(freq)

if freq.count(max_freq) > 1:
    print('?')
else:
    max_char = alphabet[freq.index(max_freq)]
    print(max_char)
