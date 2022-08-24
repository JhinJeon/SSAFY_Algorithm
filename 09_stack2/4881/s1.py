# 배열 최소 합
import sys

sys.stdin = open('sample_input.txt')


def permutations(arr):
    if len(arr) >= n:
        return num

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            arr.append(num[i])

            permutations(arr)

            visited[i] = False
            arr.pop()

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    graph = [list(map(int,input().split())) for _ in range(n)]
    answer = [0] * n
    num = list(range(n))
    visited = [[False] * n]

    for i in range(n):
        for row, col in enumerate():
            answer[i] += graph[col][row]


    print(f'#{tc}', min(answer))
