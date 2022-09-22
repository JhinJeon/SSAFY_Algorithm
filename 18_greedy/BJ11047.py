#  동전0

n, k = map(int,input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

coin_index = -1
coin_count = 0

while k > 0:
    pay = coins[coin_index]
    paycount = k // pay
    coin_count += paycount
    k -= pay * paycount
    coin_index -= 1

print(coin_count)