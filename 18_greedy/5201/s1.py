# 컨테이너 운반
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    containers, trucks = map(int, input().split())
    container_weights = list(map(int, input().split()))
    truck_capacity = list(map(int, input().split()))

    # 화물 무게 리스트는 무거운 순서로 정렬
    container_weights.sort(reverse=True)
    loaded = 0      # 배송 가능한 화물 무게의 총합

    while containers and trucks:
        target_item = container_weights[0]
        
        truck_available = 0
        for t in range(len(truck_capacity)):
            # 짐을 실을 수 있는 트럭 중에 적재용량이 가장 많은 트럭 고르기
            if truck_capacity[t] >= target_item and truck_capacity[t] > truck_available:
                truck_available = truck_capacity[t]     # 수송 가능 트럭의 적재용량
                truck_idx = t                           # 수송 가능 트럭의 인덱스 번호
        
        # 조건에 맞는 트럭이 있는 경우 배송 출발(리스트에서 제외)
        if truck_available:
            loaded += target_item               # 화물 무게 합산
            truck_capacity.pop(truck_idx)       # 사용한 트럭은 리스트에서 제외
        
        container_weights.pop(0)
        containers -= 1
        trucks -= 1

    print(f'#{tc}', loaded)