t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(n)]
    # 상, 하, 좌, 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 대각선 방향(왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래)
    di_x = [-1,1,-1,1]
    di_y = [-1,-1,1,1]

    # kill_vertical = 십자 모양으로 쐈을 때 파리 처치 수
    # kill_diagnal = 대각 방향으로 쐈을 때 파리 처치 수

    kill_vertical = 0
    kill_diagnal = 0

    for y in range(n):
        for x in range(n):
            # fly : 기준 좌표별로 파리 처치 수를 계산하는 임시 변수
            fly = graph[y][x]
            # 방향 설정
            for direction in range(4):
                # 반경이 m이 될 때까지 범위 확장
                for power in range(1, m):
                    nx = x + dx[direction] * power
                    ny = y + dy[direction] * power
                    # 이동한 좌표가 유효한 범위인 경우
                    if 0 <= nx < n and 0 <= ny < n:
                        fly += graph[ny][nx]
            if fly > kill_vertical:
                kill_vertical = fly

    for y in range(n):
        for x in range(n):
            # fly : 기준 좌표별로 파리 처치 수를 계산하는 임시 변수
            fly = graph[y][x]
            # 방향 설정
            for direction in range(4):
                # 반경이 m이 될 때까지 범위 확장
                for power in range(1,m):
                    nx = x + di_x[direction] * power
                    ny = y + di_y[direction] * power
                    # 이동한 좌표가 유효한 범위인 경우
                    if 0 <= nx < n and 0 <= ny < n:
                        fly += graph[ny][nx]
            if fly > kill_diagnal:
                kill_diagnal = fly

    answer = max(kill_diagnal, kill_vertical)

    print(f'#{tc} {answer}')