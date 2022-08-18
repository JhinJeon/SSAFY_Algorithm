# 길찾기
import sys
sys.stdin = open('input.txt')

def dfs(graph, start, end):
    if visited[end] == True:
        return 1
    else:
        visited[start] = True  # 현재 정점 방문처리

        for next_v in graph[start]:
            if visited[next_v]:  # 방문하지 않았다면
                return dfs(graph, next_v, end)  # 인접 정점으로 이동
        return 0




for _ in range(10):
    tc, path_count = map(int,input().split())
    node = [[] for _ in range(100)]
    visited = [False] * 100
    paths = list(map(int,input().split()))
    answer = 0

    for i in range(0,path_count*2,2):
        node[paths[i]].append(paths[i+1])


    if dfs(node, 0, 99) == 1:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')


