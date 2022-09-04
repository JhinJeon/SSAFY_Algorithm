# 삼각함수 연습

import math

# 1. 원주율(pi)
'''
pie = math.pi
print(pie)  # 15자리까지만 출력
'''

# 2. 각도 단위 변환(호도 <-> 일반 도)
# 호도법 pi == 각도법 180도
# 호도법 2pi == 각도법 360도

'''
gakdo = math.degrees(math.pi)   # 호도법 -> 각도법으로 변환
hodo = math.radians(gakdo)   # 각도법 -> 호도법으로 변환

print(hodo)     # 1파이(호도법)
print(gakdo)    # 180도(각도법)
'''

# 3. 사인, 역사인
# 역사인은 사인 값으로 도형의 각도를 계산하는 용도로 사용
# (삼각함수용 python 함수 공통) 입력하는 인수와 반환하는 값은 호도법 단위(radians)

'''
sin30 = math.sin(math.radians(30))
print(sin30)
'''

# 3.코사인

'''
cos60 = math.cos(math.radians(60))
acos60 = math.degrees(math.acos(cos60))
print(cos60)
print(acos60)
'''

# 4. 탄젠트

'''
tan45 = math.tan(math.radians(45))
atan45 = math.degrees(math.atan(tan45))

print(tan45)
print(atan45)
'''

# 5. 이차원 좌표에서의 삼각함수
# 인수는 (y좌표, x좌표 입력)
# 원점을 (0,0)으로 가정하고 계산

'''
test_tan = math.degrees(math.atan2(3, 4))

print(test_tan)
'''

# 6. 일타싸피에 적용해 보자

# 6-1. 목표구와 목표 지점 사이의 sin값, cos값 구하기

target = math.atan2(3, 4)
target_sin = math.sin(target)
target_cos = math.cos(target)
print(target_sin)
print(target_cos)

# 6-2. 타격구와 목표구 사이의 sin값, cos값 구하기

original = math.atan2(2, 3)
original_sin = math.sin(original)
original_cos = math.cos(original)
print(original_sin)
print(original_cos)

# 6-3. 타격구를 어느 각도에서 쳐야 하는지 계산하기

# target = 목표 지점(큐)
# current = 목표 지점으로 이동시키려는(간접적으로 때리려는) 공
# white = 직접 때리려는 공

target_x, target_y = 4, 3
current_x, current_y = 0, 0
white_x, white_y = -3, -2

current_x -= 2 * 0.5 * target_cos
current_y -= 2 * 0.5 * target_sin

distance_x = current_x - white_x
distance_y = current_y - white_y

if distance_x > 0 and distance_y > 0:
    degree = 90 - math.degrees(math.atan2(distance_y, distance_x))
elif distance_x > 0 and distance_y < 0:
    degree = 90 + math.degrees(math.atan2(distance_y, distance_x))
elif distance_x < 0 and distance_y < 0:
    degree = 270 - math.degrees(math.atan2(distance_y, distance_x))
elif distance_x < 0 and distance_y > 0:
    degree = 270 - math.degrees(math.atan2(distance_y, distance_x))

print(degree)

# 6-4. 타격구를 어느 정도 세게 쳐야 하는지 계산하기
# 빗변 길이 * 각도

power_x = math.cos(math.atan2(distance_y, distance_x)) * target_x / 0.5
power_y = math.sin(math.atan2(distance_y, distance_x)) * target_y / 0.5

print(power_x)
print(power_y)
