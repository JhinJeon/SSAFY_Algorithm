# 점점 커지는 당근의 개수

import sys

sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    # n = 당근 개수
    # carrots = 당근 리스트
    n = int(input())
    carrots = list(map(int,input().split()))

    # grow = 연속으로 성장한 당근 수 (최소 1)
    # growmax = grow의 최댓값 (최소 1)
    grow = 1
    growmax = 1
    for idx in range(n-1):
        # 당근이 연속으로 성장한 경우
        if carrots[idx] + 1 == carrots[idx+1]:
            grow += 1
            # 연속으로 성장한 최대 당근 수를 경신한 경우
            if grow > growmax:
                growmax = grow
        # 당근이 연속으로 성장하지 않은 경우 초기화
        else:
            grow = 1


    print(f'#{t} {growmax}')