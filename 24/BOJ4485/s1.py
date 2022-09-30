# 녹색 옷 입은 애가 젤다지?
import sys
sys.stdin = open('input.txt')
from collections import deque

# 순서대로 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

tc = 1

while True:
    n = int(input())
    # 0을 입력받은 경우 반복문 즉시 중단
    if n == 0:
        break
    cave = [list(map(int,input().split())) for _ in range(n)]       # 동굴 정보
    dp = [[0] * n for _ in range(n)]                                # DP 결과 저장용
    visited = [[False] * n for _ in range(n)]                       # 방문 여부 체크
    dp[0][0] = cave[0][0]                                           # DP의 시작점 설정
    visited[0][0] = True                                            # 시작점 방문여부 체크

    location = deque()          # 현재 위치 좌표 정보
    location.append((0, 0))     # 시작점 추가
    
    # 오른쪽 끝 지점까지 도달할 때까지 BFS 탐색
    while location:
        y, x = location.popleft()
        value = dp[y][x]     # value = dp 내 현재 위치 좌표
        
        # 다음 이동 방향 & 좌표 결정
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 유효한 인덱스 범위인 경우
            if 0 <= nx < n and 0 <= ny < n:
                next_value = value + cave[ny][nx]
                # 방문한 적이 있고 최솟값 경신이 불가능한 경우 continue
                if visited[ny][nx] and dp[ny][nx] <= next_value:
                    continue
                # 그 외의 경우 계산 결과를 dp에 반영한 후 방문 처리
                visited[ny][nx] = True
                dp[ny][nx] = next_value
                location.append((ny, nx))

    # dp의 목적지 좌표에 저장된 결과 출력
    answer = dp[-1][-1]

    print(f'Problem {tc}:', answer)
    tc += 1