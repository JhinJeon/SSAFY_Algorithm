# 전기버스
import sys
sys.stdin = open('sample_input.txt')

t = int(input())


# 버스의 배터리 교환 횟수를 계산하는 bus_charge 함수 정의
def bus_charge(k, charge_count, answer): # k = 충전 위치 인덱스, battery = 현재 충전소의 보유 배터리
    global answer_min   # answer_min = 충전 횟수 중 최솟값
    battery = charge_info[k]    # battery = 정류장 배터리의 성능

    # 현재 위치에서 최대한 멀리 갈 수 있는 정류장부터 탐색
    for next_charge in range(k + battery, k, -1):   
        if next_charge + 1 >= bus_stops: # 배터리 충전 후 종점까지 갈 수 있는 경우
            if answer < answer_min:    # 새로운 최솟값인 경우 answer_min 값 경신
                answer_min = answer
            return
        else:   # 일반적으로 배터리를 교환하는 경우
            answer += 1
            if answer < answer_min:     # 충전 횟수가 최소 기록보다 적은 경우에만 계산(백트래킹)
                bus_charge(next_charge, charge_count + 1, answer)
        answer -= 1


for tc in range(1, t+1):
    charge_info = list(map(int, input().split()))   # 버스 정류장과 충전소 정보 값을 한 번에 받음
    bus_stops = charge_info.pop(0)  # 입력받은 값의 첫 번째 값은 버스 정류장 숫자로 분리
    answer_min = bus_stops
    bus_charge(0, charge_info[0], 0)

    print(f'#{tc}', answer_min)