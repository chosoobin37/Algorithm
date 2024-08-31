import sys
input = sys.stdin.readline

dna, length = map(int, input().split())
dnas = []

for i in range(dna):
    atgc = input().strip()
    dnas.append(atgc)

result_dna = []
distance_sum = 0

for i in range(length):
    count = {'A': 0, 'T':0, 'G':0, 'C':0}

    for j in range(dna):
        count[dnas[j][i]] += 1

    max_char = max(count, key=lambda x: (count[x], -ord(x)))
    result_dna.append(max_char)

    distance_sum += dna - count[max_char]

print("".join(result_dna))
print(distance_sum)