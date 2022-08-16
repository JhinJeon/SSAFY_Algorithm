# 태보태보 총난타

# reverse() 활용

# 얼굴 겉 모양(겉 모양을 인식하면 반복문을 종료하기 위함)
face = ['(',')']

# action : 특수문자로 구성된 문자열을 받는 변수
# left_fist : 왼쪽 주먹을 세는 용도
# right_fist : 오른쪽 주먹을 세는 용도
# split()을 쓰지 않으면 문자열을 하나씩 나눠서 리스트에 저장(공백 포함)
action = list(input())
left_fist = 0
right_fist = 0

# 왼쪽 주먹을 세는 반복문
for act in action:
    if act == '(':
        break
    if act == '@':
        left_fist += 1

action.reverse()
# 오른쪽 주먹을 세는 반복문
for act in action:
    if act == ')':
        break
    if act == '@':
        right_fist += 1

print(left_fist, right_fist)
