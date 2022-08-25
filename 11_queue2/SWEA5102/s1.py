# 노드의 거리
import sys
sys.stdin = open('sample_input.txt')


# 시작 지점에서 끝 지점까지 몇 마디가 떨어져 있는지 반환하는 bfs 함수
def bfs(start_node, end_node):      # 시작 지점, 끝 지점 입력
    visited[start_node] = True      # 방문 여부 확인
    queue_status = [start_node]     # 다른 노드와의 연결 상태를 나타내는 큐
    search_trial = 0    # 탐색 깊이
    while queue_status:
        search_trial += 1   # 탐색 깊이 계산

        # 시작점으로부터 같은 깊이(거리)에 있는 노드들 모두 확인
        for _ in range(len(queue_status)):
            network_status = queue_status.pop(0)    # 큐에서 기준 노드 번호 반환
            for next_network in network[network_status]:    # 인접한 다른 노드들 하나씩 탐색
                if not visited[next_network]:   # 방문 기록이 없는 경우 큐에 추가
                    queue_status.append(next_network)
                    visited[next_network] = True

        # 탐색 범위 안에 목적지가 있는 경우 탐색 깊이 반환
        if end_node in queue_status:
            return search_trial
    return 0    # 경로를 못 찾은 경우 0 반환

t = int(input())

for tc in range(1,t+1):
    v, e = map(int,input().split())     # v = 네트워크 수, e = 연결된 관계 수
    network = [[] for _ in range(v+1)]  # 각 노드의 연결 상태 정보
    visited = [False] * (v+1)   # 방문 여부
    
    # network 리스트에 연결 정보 추가
    for _ in range(e):
        a, b = map(int,input().split())
        network[a].append(b)
        network[b].append(a)
    start, end = map(int,input().split())   # 시작 노드, 목표 노드

    print(f'#{tc}', bfs(start, end))