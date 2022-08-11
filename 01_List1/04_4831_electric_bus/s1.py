import sys

sys.stdin = open("sample_input.txt")

t = int(input())

# 종점부터 기점까지 사용 가능한 충전소 역산

for tc in range(1, t + 1):
    # k = 항속 거리(정류장 수)
    # n = 종점 정류장 번호(정차하는 정류장 수)
    # m = 충전소가 설치된 정류장 수
    k, n, m = map(int, input().split())
    
    # charge = 충전기가 설치된 정류장 번호
    # charge_count = 충전 횟수
    # bus_position = 버스 위치(기본값 : 종점)
    charge = list(map(int, input().split()))
    charge_count = 0
    bus_position = n

    # 운행 가능한 경우(available) 종점에서 기점까지 충전 루트 계산 반복
    available = True
    while available:
        # 버스 위치가 항속거리 이하인 경우(기점까지 도착한 경우) 반복 종료
        if bus_position <= k:
            break
            
        # 아직 기점까지 도착하지 않은 경우
        for power in range(m):
            # 사용 가능한 다음 충전소가 버스 위치보다 뒤에 있는 경우
            # (기점 방향으로 사용 가능한 충전소가 없는 경우) 운행 불가
            if charge[power] >= bus_position:
                available = False
                charge_count = 0
                break
            # 이용 가능한 충전소 중 기점에서 가장 가까운 충전소를 찾는 경우
            if bus_position <= charge[power] + k:
                charge_count += 1
                bus_position = charge[power]
                break
        # 마지막 정류장~종점 사이의 거리가 버스 항속거리보다 긴 경우
        else:
            available = False
            break

    print(f'#{tc} {charge_count}')

'''
추가 : 아직 기점까지 도착하지 않은 경우(30번째 줄 이하)를 다른 방식으로 구현하기

for power in range(len(charge)):
    if bus_position <= charge[power] + k:
        charge_count += 1
        bus_position = charge[power]
        break
    else:
        available = False
        break
'''
