# 쇠막대기 자르기
# 제한시간 초과
import sys

sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t + 1):
    placement = input()
    placement_items = len(placement)
    steels = [0] * placement_items
    laser_position = [0] * placement_items
    answer = 0

    for i in range(placement_items):
        if placement[i] == '(':
            if placement[i + 1] == '(':
                answer += 1
                for k in range(i, placement_items):
                    steels[k] += 1

            else:
                laser_position[i] += 1

        else:
            if placement[i - 1] == ')':
                for k in range(i + 1, placement_items):
                    steels[k] -= 1

    for i in range(placement_items):
        if steels[i] > 0 and laser_position[i] > 0:
            answer += steels[i]

    print(f'#{tc} {answer}')
