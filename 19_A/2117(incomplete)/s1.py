# 홈 방범 서비스
import sys
sys.stdin = open('sample_input.txt')

# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# BFS 기반 탐색
def sentry(center_x, center_y):
    pay_sum = 0  # 영역 내 수익
    homecount = 0      # 집 개수 확인
    width = 1   # 탐색 영역의 너비(가로/세로 기준)
    boundary = [(center_y, center_x)]   # 영역 가장자리의 좌표
    visited = []    # 방문한 좌표 확인용
    pay_case = []
    homecase = []

    # 추가 탐색 가능 영역이 있으면서 여유 너비가 있는 경우
    while boundary and width < n+1:
        for _ in range(len(boundary)):
            x, y = boundary.pop(0)
            visited.append((y, x))

            # 집이 있으면 수익 wtp만큼 가산
            if array[y][x] == 1:
                pay_sum += wtp
                homecount += 1
            pay_sum -= 1

            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx < n and 0 <= ny < n and (ny, nx) not in boundary and (ny, nx) not in visited:
                    boundary.append((ny, nx))
        width += 1
        pay_case.append(pay_sum)
        homecase.append(homecount)

    value = min(pay_case)
    idx = pay_case.index(value)
    hcount = homecase[idx]
    return value, hcount


t = int(input())

for tc in range(1,t+1):
    n, wtp = map(int,input().split())
    array = [list(map(int,input().split())) for _ in range(n)]      # 방범 대상 구역
    answer = 0
    pay_max = 0
    for col in range(n):
        for row in range(n):
            result = sentry(row, col)
            if result[0] > pay_max:
                answer = result[1]

    if answer == 0:
        answer = -1
    print(f'#{tc}', answer)