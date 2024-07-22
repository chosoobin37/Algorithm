# a, b, c = map(int, input().split())
# print((a**b)%c)

# a, b, c=map(int, input().split())
# for i in range(b):
#     a=a*a
# print(a%c)

a, b, c=map(int, input().split())
print(pow(a, b, c))
