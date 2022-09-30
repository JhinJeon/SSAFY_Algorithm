# 원자 소멸 시뮬레이션
import sys
sys.stdin = open('sample_input.txt')

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
        particle_position.append([col, row, kinetic])     # 방향 정보 추가(세로, 가로, 에너지 보유량)
        # 이동 방향은 0 = 상, 1 = 하, 2 = 좌, 3 = 우
        direction.append(dir)

    while away < particle_count:
        after_movement = []     # 좌표 중복 확인용
        for i in range(particle_count):
            c, r, k = particle_position[i]      # y축, x축, 에너지량

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
                particle_position[i][2] = 0
                away += 1

            # 유효하지 않은 좌표여도 일단 추가(충돌 계산용)
            particle_position[i][0] = c
            particle_position[i][1] = r
            after_movement.append((c, r))

            # 충돌(좌표 중복)이 발생한 경우
            for particle in after_movement:
                if after_movement.count(particle) > 1:
                    # 좌표가 겹치는 모든 원소의 에너지 압수
                    for i in range(particle_count):
                        column = particle_position[i][0]
                        row = particle_position[i][1]
                        energy = particle_position[i][2]

                        if (column, row) == particle:
                            # 좌표 값은 다른 좌표와 충돌하지 않도록 임의의 값으로 대체
                            particle_position[i][0] = -65535
                            particle_position[i][1] = -65535
                        
                            # 에너지 합산 후 0으로 만들기
                            answer += energy
                            particle_position[i][2] = 0
                            away += 1

    print(f'#{tc}', answer)
