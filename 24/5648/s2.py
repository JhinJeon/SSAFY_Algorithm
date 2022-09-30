# 원자 소멸 시뮬레이션
# 오답 (24/50)

import sys
sys.stdin = open('debug.txt')

t = int(input())

for tc in range(1,t+1):
    particle_count = int(input())

    particle_position = []                     # 원소 위치만 표시
    direction = []                             # 이동 방향
    kinetic_value = []                         # 에너지 보유량
    away = 0                                   # 충돌하거나 범위 밖으로 벗어난 원소 개수
    answer = 0                                 # 방출되는 에너지 총합

    for _ in range(particle_count):
        row, col, dir, kinetic = map(int, input().split())
        particle_position.append([col, row])     # 방향 정보 추가(세로, 가로, 에너지 보유량)
        # 이동 방향은 0 = 상, 1 = 하, 2 = 좌, 3 = 우
        direction.append(dir)
        kinetic_value.append(kinetic)

    while away < particle_count:
        after_movement = []     # 좌표 중복 확인용
        for i in range(particle_count):
            c, r = particle_position[i]      # y축, x축
            k = kinetic_value[i]

            # 유효하지 않은 원소인 경우 계산하지 않음
            if k == 0:
                after_movement.append((-65535, -65535))
                continue
                
            # 방향 별 이동 위치 계산
            if direction[i] == 0:               # 위쪽 이동인 경우(0)
                c += 1
            elif direction[i] == 1:             # 아래쪽 이동인 경우(1)
                c -= 1
            elif direction[i] == 2:             # 왼쪽 이동인 경우(2)
                r -= 1
            else:                               # 오른쪽 이동인 경우(3)
                r += 1

            # 범위 바깥으로 벗어난 경우
            if c < -1000 or c > 1000 or r < -1000 or r > 1000:
                kinetic_value[i] = 0
                away += 1

            # 유효하지 않은 좌표여도 일단 추가(충돌 계산용)
            particle_position[i] = (c, r)

            # 중복 체크
            if (c, r) in after_movement:
                # 좌표가 겹치는 모든 원소의 에너지 압수
                for i in range(particle_count):
                    column, row = particle_position[i]
                    energy = kinetic_value[i]

                    if (column, row) == (c, r):
                        # 좌표 값은 다른 좌표와 충돌하지 않도록 임의의 값으로 대체
                        particle_position[i] = (-65535, -65535)

                        # 에너지 합산 후 0으로 만들기
                        answer += energy
                        kinetic_value[i] = 0
                        away += 1

            # 체크 후에도 남겨두기(다중 충돌 케이스 대비용)
            after_movement.append((c, r))

    print(f'#{tc}', answer)
