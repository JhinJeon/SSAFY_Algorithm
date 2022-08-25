# 케빈 베이컨의 6단계의 법칙
# 알고리즘은 잘 썼는데 출력값을 사람 번호가 아니라 단계 횟수로 함

import sys
sys.stdin = open('input.txt')


def bfs(person_id):
    visited[person_id] = True
    friend_queue = [person_id]
    total = 0
    bacon_depth = -1
    while friend_queue:
        bacon_depth += 1
        for bacon_distance in range(len(friend_queue)):
            near_friend = friend_queue.pop(0)
            for next_person in relationship[near_friend]:
                if not visited[next_person]:
                    visited[next_person] = True
                    friend_queue.append(next_person)
            total += bacon_depth
    return total


n, m = map(int,input().split())
relationship = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    relationship[a].append(b)
    relationship[b].append(a)

result = []
for person in range(1,n+1):
    visited = [False] * (n+1)
    result.append(bfs(person))

print(result.index(min(result)) + 1)
