# 태보태보 총난타

# 슬라이싱 개념 활용

# 주먹 개수를 세는 fist_count 함수 정의
def fist_count(actions):
    fist = 0
    for act in actions:
        if act == '@':
            fist += 1
    return fist

# 얼굴의 일부('0')를 기준으로 문자열을 두 개로 분리
action_left, action_right = input().split('0')

# 분리된 문자열에 대해 각각 함수 실행 후 값 반환
left_fist = fist_count(action_left)
right_fist = fist_count(action_right)

print(left_fist, right_fist)
