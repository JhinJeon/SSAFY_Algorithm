# 바이러스
# 틀렸습니다 가 나오는 이유? = 경로가 이어져 있음에도 감염되지 않는 케이스가 나오면 카운트하지 않는 문제가 있음
# 재귀함수를 쓰는 게 아니면 deque 라이브러리를 불러와서 사용하는게 편함


# 컴퓨터 수, 인접한 경로 개수, 인접한 경로 모음 입력
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# visited = 컴퓨터 번호마다 감염 여부 확인(1 = 감염)
# total = 1번 컴퓨터를 제외한 감염된 컴퓨터 수
visited = [False] * (n + 1)
visited[1] = True
total = 0

# 각 컴퓨터 번호마다 인접한 다른 컴퓨터 확인
# 감염된 컴퓨터와 인접한 경우 감염 처리, 감염 카운트 +1
for v in range(n + 1):
    if visited[v] == True:
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = True
                total += 1

print(total)
