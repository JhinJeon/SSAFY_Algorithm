# 홈 방범 서비스
import sys
sys.stdin = open('sample_input.txt')

# 순서대로 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


# 해당 좌표의 반경 k 이내 마름모꼴 범위 탐색
def sentry(center_x, center_y, k):
    homecount = 0
    for (y, x) in home_index:
        if abs(center_x - x) + abs(center_y - y) < k:
            homecount += 1
    return homecount


t = int(input())

for tc in range(1, t+1):
    n, wtp = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]      # 방범 대상 구역

    # 집의 좌표 모아두기
    home_index = []
    for col in range(n):
        for row in range(n):
            if array[col][row] == 1:
                home_index.append((col, row))
    pay_max = wtp * len(home_index)     # 전 구역 최대 지불 능력

    # 너비, 가로, 세로 반복문을 돌면서 최대 집 수 반환
    answer = 0      # 커버 가능한 가구 수
    for width in range(n*2, 0, -1):
        cost = width * width + (width-1) * (width-1)
        for col in range(n):
            for row in range(n):
                # 손해 발생이 확정이면 탐색하지 않음
                if cost > pay_max:
                    continue
                result = sentry(col, row, width)
                # 손해가 발생하지 않은 경우 answer 경신
                if answer < result and result * wtp >= cost:
                    answer = result
        if answer:  # 현재 너비에서 최대 집 수를 찾은 경우 반복 중단
            break

    print(f'#{tc}', answer)
