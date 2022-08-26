# 농작물 수확하기
import sys
sys.stdin = open('input.txt')

# 순서대로 상, 하, 좌, 우
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


# bfs 방식
def harvest(y, x, power):
    result = 0
    depth = 0
    queue_status = [(y, x)]
    while queue_status:
        if depth == power:
            break
        for _ in range(len(queue_status)):
            y, x = queue_status.pop(0)
            result += farm[y][x]
            farm[y][x] = 0
            for direction in range(4):
                for p in range(power+1):
                    nx = x + dx[direction] * p
                    ny = y + dx[direction] * (power - p)
                    if 0 <= nx < n and 0 <= ny < n:
                        queue_status.append((ny, nx))
        depth += 1
    return result


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    farm = [list(map(int,input())) for _ in range(n)]
    center = n // 2
    print(f'#{tc}', harvest(center, center, center))