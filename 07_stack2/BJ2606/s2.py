# 바이러스
# 틀렸습니다 가 나오는 이유?


# 컴퓨터 수, 인접한 경로 개수, 인접한 경로 모음 입력
computers = int(input())
network = int(input())
network_connection = [[] for _ in range(computers + 1)]

for i in range(network):
    a, b = map(int, input().split())
    network_connection[a].append(b)
    network_connection[b].append(a)

# virus_visited = 컴퓨터 번호마다 감염 여부 확인(1 = 감염)
# answer = 1번 컴퓨터를 제외한 감염된 컴퓨터 수
virus_visited = [0] * (computers + 1)
virus_visited[1] = 1
answer = 0

# 각 컴퓨터 번호마다 인접한 다른 컴퓨터 확인
# 감염된 컴퓨터와 인접한 경우 감염 처리, 감염 카운트 +1
for computer_no in range(1, computers + 1):
    if virus_visited[computer_no] == 1:
        for next_visit in network_connection[computer_no]:
            if virus_visited[next_visit] == 0:
                virus_visited[next_visit] = 1
                answer += 1

print(answer)
