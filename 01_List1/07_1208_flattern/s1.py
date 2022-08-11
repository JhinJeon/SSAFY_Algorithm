import sys

sys.stdin = open("input.txt")

for tc in range(1,11):
    # dump_count : 덤프 가능 횟수
    # boxes : 상자 배치 상태
    dump_count = int(input())
    boxes = list(map(int,input().split()))
    
    # 상자의 최고 높이와 최저 높이 파악
    # dump_count가 0일 때도 계산하는 이유는 코드 최적화를 위함
    while dump_count >= 0:
        lowest = 0
        highest = 0
        # 상자의 최고 높이와 최저 높이 파악(min, max 대신 완전탐색 사용)
        # dump 이후 boxes의 값을 변경해야 하므로 리스트 인덱스를 이용해 구현
        for b in range(len(boxes)):
            if boxes[b] > boxes[highest]:
                highest = b
            if boxes[b] < boxes[lowest]:
                lowest = b
        # dump_count가 0인 경우 최고 위치와 최저 위치를 파악해서 그 차이값 반환
        if dump_count == 0:
            gap = boxes[highest] - boxes[lowest]
            break

        # 아직 dump_count가 남아 있을 경우 상자 위치 이동, dump_count 차감
        boxes[highest] -= 1
        boxes[lowest] += 1
        dump_count -= 1


    print(f'#{tc} {gap}')