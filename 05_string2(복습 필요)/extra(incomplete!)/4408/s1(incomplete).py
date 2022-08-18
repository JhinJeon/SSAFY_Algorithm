# 자기 방으로 돌아가기
import sys
sys.stdin = open('sample_input.txt')

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
        ends.append(end)
    
    # trials = 방을 이동하는데 필요한 시간 단위
    trials = 0
    for i in range(n):
        # 이동 경로가 겹치는 경우
        for j in range(n):
            if i == j:
                continue
            if starts[i] <= starts[j] <= ends[i] or starts[i] <= ends[j] <= ends[i]:
                trials += 1

    if trials > 0:
        answer = trials // 2
    else:
        answer = 1

    print(f'#{tc} {answer}')
        