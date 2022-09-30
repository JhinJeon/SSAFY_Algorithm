# DFS
import sys
sys.stdin = open('test1.txt')


def dfs(start):
    visited[start] = True       # 현재 위치 방문 처리
    search_result.append(start)     # 탐색 결과에 저장
    # 인접한 노드들 중 아직 방문하지 않은 노드들부터 방문
    for next_node in connection[start]:
        if not visited[next_node]:
            dfs(next_node)


input_data = list(map(int,input().split()))

max_no = len(input_data)//2
connection = [[] for _ in range(max_no)]
visited = [False] * (max_no + 1)
search_result = []

# 현재 노드 위치에서 인접한 모든 노드 정보 저장
for i in range(0, len(input_data), 2):
    connection[input_data[i]].append(input_data[i+1])
    connection[input_data[i+1]].append(input_data[i])

dfs(1)
print(*search_result)