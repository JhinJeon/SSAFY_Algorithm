# 부분집합의 합계

import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    numbers = list(map(int, input().split()))
    n = len(numbers)
    # answer = 부분집합의 합이 0인지 아닌지를 저장하는 변수(1 == True, 0 == False)
    answer = 0

    for i in range(1, 1 << n):
        # sum_temp = 부분집합의 합계를 저장하는 임시 변수
        sum_temp = 0

        # numbers 리스트의 비트 이동
        for j in range(n):
            # i와 j칸만큼 이동한 비트가 동일한 경우(서로 다른 값인 경우) 부분집합 합계에 추가
            if i & (1 << j):
                sum_temp += numbers[j]
        # 원소의 합이 0인 부분집합이 발견되는 경우
        if sum_temp == 0:
            answer = 1

    print(f'#{tc} {answer}')
