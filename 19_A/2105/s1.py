# 디저트 카페
import sys
sys.stdin = open('sample_input.txt')

# 순서대로 우하, 좌하, 좌상, 우상
dx = [1, -1, -1, 1]
dy = [1, 1, -1, -1]


# DFS 탐색
def cafe_tour(y, x, direction, depth):
    # answer = 이동 횟수, dessert_visited = 중복 방문 확인
    global answer, dessert_visited

    # 현재 위치가 모서리인 경우
    if y == 0 or y == n-1:
        if x == 0 or x == n-1:
            return

    # 다음 이동 방향 결정
    for d in range(direction, direction + 2):       # 직진 or 90도 꺾기만 고려
        if d > 3:   # 유효한 인덱스 범위를 벗어난 경우
            return
        nx = x + dx[d]
        ny = y + dy[d]
        # 유효한 좌표인 경우
        if 0 <= nx < n and 0 <= ny < n:
            # 시작 지점으로 되돌아간 경우
            if (ny, nx) == start:
                # 최대 깊이를 경신하는 경우
                if depth > answer:
                    answer = depth
                return
            # 아직 (값 기준) 방문하지 않은 지역인 경우
            elif not dessert_visited[cafe_map[ny][nx]]:
                # 이동할 위치의 값 방문 처리 후 재귀 탐색
                dessert_visited[cafe_map[ny][nx]] = True
                cafe_tour(ny, nx, d, depth + 1)
                
                # 탐색 과정 원상복귀
                dessert_visited[cafe_map[ny][nx]] = False


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    cafe_map = [list(map(int,input().split())) for _ in range(n)]
    answer = 0      # 최대 이동 횟수
    dessert_visited = [False] * 101     # 중복 방지용 리스트
    for col in range(n):
        for row in range(n):
            start = (col, row)
            # 시작점 방문 처리
            dessert_visited[cafe_map[col][row]] = True
            cafe_tour(col, row, 0, 1)
            # 원상복귀
            dessert_visited[cafe_map[col][row]] = False

    # 값이 갱신된 적이 없으면(유효한 경로가 하나도 없으면) -1 반환
    if answer == 0:
        answer = -1
    print(f'#{tc}', answer)
