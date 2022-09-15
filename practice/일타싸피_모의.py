import math

pocket_x, pocket_y = 6, 8
target_x, target_y = 0, 0
white_x, white_y = 3, -4
ball_radius = 1  # 반지름 길이

# 1. 목표구와 포켓 사이의 거리 계산

distance_x = pocket_x - target_x
distance_y = pocket_y - target_y

# 1-1 : 목표구와 포켓의 삼각함수 각도 계산

degree_pocket = math.atan2(distance_y, distance_x)
degree_x = math.cos(degree_pocket)
degree_y = math.sin(degree_pocket)

# 1-2 : 타격구의 목표 좌표 계산

target_x -= 2 * ball_radius * degree_x
target_y -= 2 * ball_radius * degree_y

print(target_x)
print(target_y)

# 2. 타격구를 어떤 각도로 쳐야 하는지 계산

attack_x = target_x - white_x
attack_y = target_y - white_y

hit_degree = math.atan2(attack_y, attack_x)


# 2-1. 각도 계산

# 각도는 수직(12시 방향)이 0도임
# 1사나 4사면 90도(오른쪽 수평)을 기준으로 계산
# 2사나 3사면 270도(왼쪽 수평)을 기준으로 계산

degree = 270 - math.degrees(math.atan2(attack_y, attack_x))

if degree <= 90:
    print(degree)
else:
    print(180 - degree)

# 3. 타격구를 어느 정도의 세기로 쳐야 하는지 계산

# 공 반지름 * 목표구(타격 지점)~포켓 간 각도(사인값/코사인값)
power_x = pocket_x * \
    math.sin(math.atan2(distance_y, distance_y)) / ball_radius
power_y = pocket_y * \
    math.cos(math.atan2(distance_y, distance_x)) / ball_radius

print(power_x)
print(power_y)

# 유의사항

# 파일명과 코드 내 개인정보 : 지역_이름(영문 대문자로)
# zip파일로 압축해서 제출
# 어떤 전략으로 알고리즘을 구성했는지 .txt파일로 설명 추가
