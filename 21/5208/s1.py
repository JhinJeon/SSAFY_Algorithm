# 전기버스 2
import sys
sys.stdin = open('sample_input.txt')


# dfs 기반 최소 충전 횟수를 반환하는 함수 bus
def bus(location, chargecount):
    global answer
    # 종점에 도착한 경우
    if location >= stops - 1:
        # 최솟값 경신인 경우 교환 횟수에 반영
        if chargecount < answer:
            answer = chargecount
        return

    # 최솟값을 경신할 여지가 없는 경우(백트래킹)
    if chargecount > answer:
        return

    remain = charge_info[location]     # 현재 위치에서 배터리 교환
    # 추가로 갈 수 있는 경우의 수 탐색(뒤쪽부터)
    # 뒤쪽부터 탐색하지 않으면 제한시간 초과 발생
    for next_stop in range(stops-1, location, -1):
        if location + remain >= next_stop:
            bus(next_stop, chargecount + 1)


t = int(input())

for tc in range(1, t+1):
    input_data = list(map(int, input().split()))
    stops = input_data[0]           # 정류장 수
    charge_info = input_data[1:]    # 정류장 별 배터리 정보
    answer = stops                     # 충전 횟수(최대 횟수는 정류장 수에 비례)

    bus(0, -1)

    print(f'#{tc}', answer)
