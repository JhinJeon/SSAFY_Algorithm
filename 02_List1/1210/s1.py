# ladder 1
# 재귀함수는 최대 깊이 도달!
import sys
sys.stdin = open('input.txt')


def ladder(graph, start, x_location, y_location):
    for i in range(4):
        if x_location == 99 and y_location == 99:
            return start
        nx = x_location + dx[i]
        ny = y_location + dy[i]
        if 0 <= nx < 100 and 0 <= ny < 100:
            ladder(graph, start, nx, ny)
        else:
            continue

t = int(input())

for tc in range(1,t+1):
    ladder_graph = [list(map(int,input().split())) for _ in range(100)]
    
    # 상, 하, 좌, 우 이동을 dx, dy로 표현
    # y가 세로(column), x가 가로(row)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for starting_point in range(100):
        answer = ladder(ladder_graph, starting_point, starting_point, 0)
        if answer is not None:
            print(f'#{tc} {answer}')






