# BFS
import sys
sys.stdin = open('test1.txt')

from collections import deque


def bfs(start):
    visited[start] = True       # 현재 위치 방문 처리
    search_result = [start]          # 탐색 결과
    queue = deque()             # 탐색 과정 중간 저장용
    queue.append(start)
    
    # queue에 탐색할 노드가 있는 동안 반복
    while queue:
        current_node = queue.popleft()      # 가장 맨 왼쪽 값을 pop
        # 현재 노드의 인접 노드들 중 방문하지 않은 노드를 queue에 추가
        for next_node in connection[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                search_result.append(next_node)
                queue.append(next_node)

    return search_result


input_data = list(map(int,input().split()))

max_no = len(input_data)//2
connection = [[] for _ in range(max_no)]
visited = [False] * (max_no + 1)

# 현재 노드 위치에서 인접한 모든 노드 정보 저장
for i in range(0, len(input_data), 2):
    connection[input_data[i]].append(input_data[i+1])
    connection[input_data[i+1]].append(input_data[i])

answer = bfs(1)
print(*answer)