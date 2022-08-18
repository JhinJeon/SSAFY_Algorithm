# 제로

k = int(input())
money = [0] * k
top = 0

for t in range(k):
    money_input = int(input())
    if money_input == 0:
        top -= 1
        money[top] = 0
    else:
        money[top] = money_input
        top += 1
print(sum(money))
