# sum

import sys
sys.stdin = open("input.txt")

for tc in range(10):
    case = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]
    result = []

    for row in range(100):
        # 열 방향 합계
        result.append(sum(numbers[row][:]))
        # 행 방향 합계
        col_temp = 0
        for col in range(100):
            col_temp += numbers[col][row]
        result.append(col_temp)
    # 왼쪽 위에서 사선 방향
    diagnal_lt_rb = 0
    # 오른쪽 위에서 사선 방향
    diagnal_rt_lb = 0
    for i in range(100):
        diagnal_lt_rb += numbers[i][i]
    for i in range(100):
        diagnal_rt_lb += numbers[i][-1-i]
    result.append(diagnal_rt_lb)
    result.append(diagnal_lt_rb)

    # 최고값 구하기
    max_value = max(result)
    print(f'#{case} {max_value}')
