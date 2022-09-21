import sys
sys.stdin = open('sample_input.txt')


# 순서대로 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def search_path(y, x, value):
    global answer
    visited[y][x] = True    # 방문 처리

    # 최솟값을 경신할 가능성이 없는 경우 이전 레벨로 복귀
    if answer < value:
        return
    # 목적지인 경우 값 추가
    if y == n-1 and x == n-1:
        if answer > value:
            answer = value
        return

    # 새로운 이동 방향 탐색
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 유효한 범위의 인덱스이면서 아직 방문하지 않은 지역인 경우
        if x <= nx < n and y <= ny < n and not visited[ny][nx]:
            # 이동할 위치의 값 합산
            value += graph[ny][nx]

            # 재귀 호출
            search_path(ny, nx, value)

            # 이후 방문 여부 초기화
            value -= graph[ny][nx]
            visited[ny][nx] = False


t = int(input())

for tc in range(1, t+1):
    n = int(input())        # 이차원 배열의 가로, 세로 길이
    graph = [list(map(int, input().split())) for _ in range(n)]     # 이차원 배열 정보
    visited = [[False] * n for _ in range(n)]           # 방문 여부 확인용

    val = graph[0][0]     # 시작점의 값
    answer = 10 * (n ** 2)   # 경로 합계

    search_path(0, 0, val)

    print(f'#{tc}', answer)
