a=int(input())
b=int(input())

# print(a*(b%10),a*(int((b%100)/10)), a*(int(b/100)), a*b, sep='\n')

# b를 문자열로 변환한 후 각 자릿수를 정수로 변환해 
second=[int(digit) for digit in str(b)]

print(a*second[0], a*second[1], a*second[2], a*b, sep='\n')