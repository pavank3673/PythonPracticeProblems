from random import randint

stake = int(input("Enter stake $ :"))
goal = int(input("Enter goal $ :"))
n = int(input("Enter no of times : "))

win_count = 0
bet_count = 0
i = 1

while(i <= n):
    if stake == 0 or stake == goal:
        break
    bets = 1
    bet_count += 1
    bet_result = randint(0, 1)
    if bet_result == 1:
        win_count += 1
        stake = stake + bets
    else:
        stake = stake - bets
    i += 1

win_percentage = (win_count / bet_count) * 100
loss_percentage = 100 - win_percentage

print(f"Number of wins : {win_count}, Percentage of win :{win_percentage}, Percentage of loss : {loss_percentage}")

