# 회의실 배정
# 화물 도크와 유사한 구성

import sys
sys.stdin = open('testcase.txt')


def dock_management(k, event):
    global answer
    # 최댓값 경신인 경우 answer에 저장
    if event > answer:
        answer = event

    # 현재 일정의 종료 시각
    end_time = timeline[k][1]

    for i in range(n):
        # 다음 일정이 현재와 겹치지 않고 아직 처리되지 않은 경우
        if timeline[i][0] >= end_time:
            dock_management(k, event + 1)
            event -= 1


n = int(input())
timeline = [list(map(int, input().split())) for _ in range(n)]
timeline.sort(key=lambda x:x[0])
answer = 0

for start_idx in range(n):
    dock_management(timeline[start_idx][0], 1)

print(answer)