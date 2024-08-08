# game, win = map(int, input().split())
# cal = win/game
# formatted_rate = str(cal)[:str(cal).find('.')+3]
# rate = int((float(formatted_rate))*100)
# new_rate = rate
# count = 0

# while True:
#     if rate == new_rate:
#         game += 1
#         win += 1
#         count += 1
#         new_rate = int((float(str(win/game)[:str(win/game).find('.')+3]))*100)
#     elif rate != new_rate:
#         print(count)
#         break
#     elif TimeoutError:
#         print(-1)

# import math

# game, win = map(int, input().split())

# current_rate = math.floor((win/game)*100)
# count = 0

# while True:
#     count += 1
#     new_game = game + count
#     new_win = win + count
#     new_rate = math.floor((new_win/new_game)*100)

#     if new_rate > current_rate:
#         print(count)
#         break

#     if count >  1000000000:
#         print(-1)
#         break

# game, win = map(int, input().split())

# current_rate = (100*win)//game
# count = 0

# while True:
#     count += 1
#     new_game = game + count
#     new_win = win + count
#     new_rate = (100*new_win)//new_game

#     if new_rate > current_rate:
#         print(count)
#         break

#     if TimeoutError: 
#         print(-1)
#         break

def min_games_needed(game, win):
    current_rate = (100*win) // game
    left, right = 0 , 2000000000

    while left <= right:
        mid = (left+right) // 2
        new_game = game + mid
        new_win = win + mid
        new_rate = (100*new_win) // new_game

        if new_rate > current_rate:
            right = mid - 1
        else:
            left = mid + 1

    if left > 2000000000:
        return -1
    else: 
        return left
    
game, win = map(int, input().split())
print(min_games_needed(game, win))