# 원자 소멸 시뮬레이션
# 오답 (24/50)
# 홀수 칸 떨어진 원자 간 충돌도 계산하기 위해 그래프 영역을 두 배로 늘리기

import sys
sys.stdin = open('sample_input.txt')

# 순서대로 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

t = int(input())

for tc in range(1, t+1):
    particle_count = int(input())
    particle_status = []                       # 원소 정보 표시
    answer = 0                                 # 방출되는 에너지 총합

    for _ in range(particle_count):
        row, col, dir, kinetic = map(int, input().split())
        row = (row + 1000) * 2      # 좌표값 보정(음수 좌표 양수로 변환, 홀수 칸 떨어진 원소 충돌 계산용)
        col = (col + 1000) * 2
        particle_status.append([row, col, dir, kinetic])     # 원소 정보 추가(가로, 세로, 방향, 에너지 보유량)

    while len(particle_status) >= 2:
        after_movement = []     # 원소의 좌표 변화 반영
        next_loc = []           # 다음에 이동할 위치(좌표만)
        hitpoint = set()    # 충돌 위치
        for i in range(len(particle_status)):
            x, y, d, val = particle_status[i]      # x축, y축, 방향, 에너지
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 밖으로 벗어난 원소는 고려 X
            if 0 <= nx <= 4000 and 0 <= ny <= 4000:
                # after_movement에 있는 좌표가 또 나오면 충돌 처리
                if (nx, ny) in next_loc:
                    hitpoint.add((nx, ny))
                # 다음 좌표 정보를 after_movement에 저장
                else:
                    next_loc.append((nx, ny))
                after_movement.append((nx, ny, d, val))

        # after_movement의 원소들을 하나씩 pop한 후 충돌 여부 검증
        particle_status = []
        for j in range(len(after_movement)):
            row, col, dir, val = after_movement[j]
            # 충돌한 원소는 에너지 합산
            if (row, col) in hitpoint:
                answer += val
            # 이상 없는 원소는 원상복귀
            else:
                particle_status.append((row, col, dir, val))

    print(f'#{tc}', answer)
