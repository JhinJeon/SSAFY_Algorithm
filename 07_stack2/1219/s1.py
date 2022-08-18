# 길찾기
# 용준님 코드 참조

import sys
sys.stdin = open('input.txt')


# 깊이 우선 탐색을 수행하는 dfs 함수 정의
def dfs(v): 
    # 현재 위치는 방문 처리
    visited[v] = True                           

    # 현재 노드의 인접 노드 조사 : 방문하지 않은 경우 방문 처리 후 재귀 실행
    for w in node[v]:                         
        if not visited[w]:                     
            v = w                          
            dfs(v)                           


for _ in range(10):
    tc, path_count = map(int,input().split())
    node = [[] for _ in range(100)]
    visited = [False] * 100
    paths = list(map(int,input().split()))
    answer = 0

    # node에 인접 노드 연결 정보 추가
    for i in range(0,path_count*2,2):
        node[paths[i]].append(paths[i+1])

    # 함수 실행(시작 지점 = 0)
    dfs(0)

    # 함수 실행 결과 도착지에 방문했으면 1 반환
    if visited[99]:
        answer = 1
    else:
        answer = 0

    print(f'#{tc} {answer}')


