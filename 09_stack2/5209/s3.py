# 최소 생산 비용
# 시간 초과

import sys
sys.stdin = open('sample_input.txt')


def permutation(sample_list, col_count):
    global result
    value = sum(sample_list)
    if len(sample_list) == n:
        if value < result:
            result = value
    for i in range(n):
        if not visited[i]:
            sample_list.append(factory[col_count][i])
            visited[i] = True

            if value <= result:
                permutation(sample_list, col_count + 1)

            visited[i] = False
            sample_list.pop()


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    factory = [list(map(int,input().split())) for _ in range(n)]
    visited = [False] * n
    result = 99 * n

    for k in range(n):  # 시간 초과의 원인
        permutation([], 0)


    print(f'#{tc}', result)

