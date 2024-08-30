import sys

input = sys.stdin.readline

broke, brand = map(int, input().split())
min_set_price = float('inf')
min_piece_price = float('inf')

for i in range(brand):
    set_price, piece_price = list(map(int, input().split()))
    min_set_price = min(min_set_price, set_price)
    min_piece_price = min(min_piece_price, piece_price)

for i in range(brand):
    cost_all_sets = (broke//6)*min_set_price + min(min_set_price, (broke%6)*min_piece_price)
    cost_all_pieces = broke * min_piece_price

print(min(cost_all_sets, cost_all_pieces))