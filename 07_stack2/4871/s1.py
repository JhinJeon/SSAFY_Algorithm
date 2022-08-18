# 그래프 경로

import sys
sys.stdin = open('sample_input.txt')

# 함수에 입력된 값부터 방문 처리하는 draw_graph 함수 정의
def draw_graph(v):
    # 현재 정점 방문처리
    visited[v] = True  

    # 인접한 정점 차례대로 방문 후 방문 처리
    for next_v in graph_status[v]:
        if not visited[next_v]:  
            draw_graph(next_v)  

t = int(input())

for tc in range(1,t+1):
    v, e = map(int,input().split())
    graph_status = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    for i in range(e):
        node, edge = map(int,input().split())
        graph_status[node].append(edge)
    start, end = map(int,input().split())

    draw_graph(start)

    # end 위치가 방문 처리된 경우 1 반환
    if visited[end] == True:
        answer = 1
    # 방문 처리되지 않은 경우 0 반환
    else:
        answer = 0

    print(f'#{tc} {answer}')

