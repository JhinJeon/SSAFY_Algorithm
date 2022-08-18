# 태보태보 총난타

# 최초 작성 코드

# 얼굴 겉 모양(겉 모양을 인식하면 반복문을 종료하기 위함)
face = ['(',')']

# action : 특수문자로 구성된 문자열을 받는 변수
# left_fist : 왼쪽 주먹을 세는 용도
# right_fist : 오른쪽 주먹을 세는 용도
action = input()
left_fist = 0
right_fist = 0

# 왼쪽 주먹을 세는 반복문
for i in range(len(action)):
    if action[i] == '(':
        break
    if action[i] == '@':
        left_fist += 1

# 오른쪽 주먹을 세는 반복문
for i in range(-1,-len(action)-1,-1):
    if action[i] == ')':
        break
    if action[i] == '@':
        right_fist += 1

print(left_fist, right_fist)
