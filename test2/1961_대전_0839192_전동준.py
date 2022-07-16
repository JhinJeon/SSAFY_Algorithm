t = int(input())
for k in range(1,t+1):
    n = int(input())
    graph = []
    print('#'+str(k))
    for i in range(n):
        graph.append(list(map(int,input().split())))
    graph90 = [[0] * n for _ in range(n)]
    graph180 = [[0] * n for _ in range(n)]
    graph270 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            graph90[i][n-1-j] = graph[j][i]
    for i in range(n):
        for j in range(n):
            graph180[i][n-1-j] = graph90[j][i]
    for i in range(n):
        for j in range(n):
            graph270[j][i] = graph[i][n-1-j]
    for i in range(n):
        print(''.join(map(str,graph90[i])),end = ' ')
        print(''.join(map(str,graph180[i])),end=' ')
        print(''.join(map(str,graph270[i])))