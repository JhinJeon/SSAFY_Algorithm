# 화물 도크
import sys
sys.stdin = open('sample_input.txt')


def dock_management(k, event, depth_remain):
    global answer
    recorded[k] = True
    # 백트래킹 요소 추가 : 최댓값 경신의 여지가 없는 경우 탐색 종료
    if depth_remain + event < answer:
        return
    # 현재 일정의 종료 시간 기록
    end_time = timeline[k][1]
    for i in range(n):
        # 다음 일정이 현재와 겹치지 않고 아직 처리되지 않은 경우
        if timeline[i][0] >= end_time and not recorded[i]:
            dock_management(i, event + 1, depth_remain - 1)
            recorded[i] = False     # 재귀 호출 후 원상복귀
    # 최댓값 경신인 경우 answer에 저장
    else:
        if event > answer:
            answer = event


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    timeline = [list(map(int,input().split())) for _ in range(n)]
    timeline.sort(key=lambda x:x[0])    # 일정표를 리스트의 첫 번째 항목을 기준으로 오름차순
    answer = 0
    recorded = [False] * n              # 방문 여부

    for i in range(n):
        dock_management(i, 1, n)

    print(f'#{tc}', answer)