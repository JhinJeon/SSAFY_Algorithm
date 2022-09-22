# 회의실 배정
# 화물 도크와 유사한 구성

def dock_management(k, event, depth_remain):
    global answer
    recorded[k] = True
    # 백트래킹 요소 추가 : 최댓값 경신의 여지가 없는 경우 탐색 종료
    if depth_remain + event < answer:
        return
    end_time = timeline[k][1]
    for i in range(k, n):
        # 다음 일정이 현재와 겹치지 않고 아직 처리되지 않은 경우
        if timeline[i][0] >= end_time and not recorded[i]:
            dock_management(i, event + 1, depth_remain - 1)
            recorded[i] = False     # 재귀 호출 후 원상복귀
    # 최댓값 경신인 경우 answer에 저장
    else:
        if event > answer:
            answer = event


n = int(input())
timeline = [list(map(int, input().split())) for _ in range(n)]
timeline.sort(key=lambda x:x[0])
answer = 0
recorded = [False] * n

for i in range(n):
    dock_management(i, 1, n)

print(answer)