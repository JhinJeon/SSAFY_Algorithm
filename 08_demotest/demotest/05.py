# 창용 마을 무리의 개수
import sys
sys.stdin = open('s5_input.txt')

def dfs(p):
    checked[p] = True
    for next_check in relations[p]:
        if not checked[next_check]:
            dfs(next_check)


t = int(input())

for tc in range(1,t+1):
    n, m= map(int,input().split())
    relations = [[] for _ in range(n+1)]
    checked = [False] * (n+1)
    for i in range(m):
        a, b = map(int,input().split())
        relations[a].append(b)
        relations[b].append(a)

    brood = 0
    for i in range(1,n+1):
        if not checked[i] and relations[i]:
            dfs(i)
            brood += 1
    for c in range(1,n+1):
        if not checked[c]:
            brood += 1

    print(f'#{tc} {brood}')