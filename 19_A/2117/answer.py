# 범위 기준점을 한가운데로 생각하고 풀어도 되나?

def operation_expense(k):
    return k * k + (k - 1) * (k - 1)


for tc in range(int(input())):
    N, M = map(int, input().split())

    field = [list(map(int, input().split())) for _ in range(N)]
    homes = []

    for y in range(N):
        for x in range(N):
            if field[y][x]:
                homes.append((y, x))

    max_profit = len(homes) * M

    for k in range(N + 2, 0, -1):   # 최대 마름모 너비부터 계산
        cur_expense = operation_expense(k)
        if max_profit - cur_expense >= 0:
            num_max_home = 0
            for y in range(N):      # y좌표 반복(0부터 n-1까지)
                for x in range(N):      # x좌표 반복(0부터 n-1까지)
                    num_home = 0        # 범위 내 방범 대상 집 개수
                    for h_y, h_x in homes:
                        if abs(y - h_y) + abs(x - h_x) < k:     # x, y좌표로부터 너비 k인 마름모 범위 내 계산
                            num_home += 1
                    if num_max_home < num_home and num_home * M >= cur_expense:     # 이익이 발생했고 집 최댓값을 경신하는 경우
                        num_max_home = num_home
            if num_max_home:    # 손해 보지 않으면서 가장 많은 집들에게 서비스 가능한 경우를 발견한 경우
                break

    print('#{} {}'.format(tc + 1, num_max_home))
