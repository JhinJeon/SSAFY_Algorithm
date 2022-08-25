def dfs(computer_id):
    global answer
    visited[computer_id] = True
    for next_computer in network_status[computer_id]:
        if not visited[next_computer]:
            answer += 1
            dfs(next_computer)


computer = int(input())
n = int(input())
answer = 0
visited = [False] * (computer + 1)
network_status = [[] for _ in range(computer+1)]

for _ in range(n):
    a, b = map(int, input().split())
    network_status[a].append(b)
    network_status[b].append(a)

dfs(1)

print(answer)