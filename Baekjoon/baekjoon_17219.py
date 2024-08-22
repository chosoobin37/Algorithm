import sys
input = sys.stdin.readline

site, find = map(int, input().split())
save = {}

for i in range(site):
    email, password = input().split()
    save[email] = password

for i in range(find):
    want = input().strip()
    if want in save:
        print(save[want])

