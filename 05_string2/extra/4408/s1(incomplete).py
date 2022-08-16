# 자기 방으로 돌아가기

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    # starts = 출발하는 방 리스트
    # ends = 도착해야 하는 방 리스트
    starts = []
    ends = []
    for _ in range(n):
        start, end = map(int, input().split())
        starts.append(start)
        ends.append(ends)
    
    # trials = 방을 이동하는데 필요한 시간 단위
    trials = 0
    for i in range(n):
        moving_route = list(starts[i], ends[i])
        for j in range(n):
            if moving_route[0] <= starts[j] <= moving_route[1] or moving_route[0] <= ends[j] <= moving_route[1]:
                trials += 1

    if trials > 0:
        answer = trials / 2
    else:
        answer = 1

    print(f'#{tc} {answer}')
        