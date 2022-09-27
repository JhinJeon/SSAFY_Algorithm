# 보급로
import sys
sys.stdin = open('input.txt')

# 순서대로 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(col, row):
    global answer
    next_visit =[(0, 0, 0, 0, 0)]   # 다음 방문 지점(행, 열, 평탄화 값, 이전 행, 이전 열)
    while next_visit:
        for _ in range(len(next_visit)):
            y, x, dig_total, y_before, x_before = next_visit.pop(0)
            # 개선의 여지가 없는 경우 탐색 중단(백트래킹)
            if dig_total > answer:
                break
            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 왔던 방향으로 되돌아가는 경우
                if ny == y_before and nx == x_before:
                    continue
                # 목적지에 도달한 경우
                if ny == n-1 and nx == n-1:
                    if answer > dig_total:
                        answer = dig_total
                    break
                # 목적지를 향해서 경로를 찾는 경우
                elif 0 <= nx < n and 0 <= ny < n:
                    next_visit.append((ny, nx, dig_total + graph[ny][nx], y, x))


t = int(input())

for tc in range(1,t+1):
    n = int(input())    # 정사각형 지도 한 변의 길이
    graph = [list(map(int, input())) for _ in range(n)]
    answer = 10 * n ** 2 # 최소 복구 시간
    bfs(0,0)
    print(f'#{tc}', answer)