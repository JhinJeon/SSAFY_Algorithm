# 격자판 숫자 이어 붙이기
# 재귀호출 할 때 ny, nx 순서를 잘못 적어서 오류 발생

import sys
sys.stdin = open('debuginput.txt')

# 순서대로 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(number, y, x):
    global case
    # 7글자를 연결한 경우
    if len(number) == 7:
        case.add(number)
        return
    
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 이동 가능하면서 아직 방문하지 않은 지역인 경우 재귀호출
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(number + board[ny][nx], ny, nx)

    return


t = int(input())

for tc in range(1, t+1):
    board = [list(map(str, input().split())) for _ in range(4)]
    case = set()  # 최종 경우의 수 저장

    for col in range(4):
        for row in range(4):
            result = []
            dfs("", col, row)

    answer = len(case)
    print(f'#{tc}', answer)