# 최소 생산 비용
# 시간 초과

import sys
from itertools import permutations
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    factory = [list(map(int,input().split())) for _ in range(n)]
    price_min = 99 * n  # 공장별 생산비용의 최댓값은 99
    for cases in permutations(list(range(n)), n):
        price_value = 0
        for col, row in enumerate(cases):
            price_value += factory[col][row]
            if price_value > price_min:
                break
        else:
            price_min = price_value

    print(f'#{tc}', price_min)

