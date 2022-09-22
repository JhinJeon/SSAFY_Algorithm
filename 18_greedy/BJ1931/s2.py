# 회의실 배정
# 람다 함수로 정렬

import sys
sys.stdin = open('testcase.txt')


n = int(input())
timeline = [list(map(int, input().split())) for _ in range(n)]      # 일정표

# 람다 함수를 이용해서 일정표 리스트를 하위 리스트의 0번 인덱스, 1번 인덱스를 기준으로 정렬
timeline.sort(key=lambda x: x[0])
timeline.sort(key=lambda x: x[1])
answer = 0          # 받은 팀 수
current_time = 0    # 현재 시각

# 현재 팀의 종료 시간 이후 다음 팀 시작 시간과 연결
for i in range(n):
    if timeline[i][0] >= current_time:
        current_time = timeline[i][1]
        answer += 1

print(answer)
