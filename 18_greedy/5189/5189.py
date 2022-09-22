# 전자카트
# dfs 방식으로 해결

import sys
sys.stdin = open('sample_input.txt')


def dfs(k, val):
    global answer
    # 최솟값 경신 여지가 없는 경우(백트래킹)
    if val > answer:
        return
    # 모든 구역을 다 방문한 뒤 출발지로 돌아온 경우
    if k == 0 and False not in visited and answer > val:
        answer = val
        return

    # 방문해야 할 곳이 남은 경우 : 다음 방문지 리스트 불러오기
    next_array = graph[k]
    for i in range(n):
        next = next_array[i]
        if next > 0 and not visited[i]:
            visited[i] = True
            dfs(i, val + next)
            visited[i] = False


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]      # 구역 정보
    visited = [False] * n                                           # 구역 별 방문 여부
    current_idx = 0                                                 # 출발 위치
    answer = (n + 1) * 100                                          # 출력할 답(기본값 = 최대치)

    dfs(current_idx, 0)

    print(f'#{tc}', answer)