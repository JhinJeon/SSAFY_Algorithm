# 태보태보 총난타

# 반복문을 하나로 압축한 형태

# action : 특수문자로 구성된 문자열을 받는 변수
# left_fist : 왼쪽 주먹을 세는 용도
# right_fist : 오른쪽 주먹을 세는 용도
# face_passed : 반복문 탐색이 얼굴을 지나쳤는지 확인하는 용도(False = 왼쪽, True = 오른쪽)
action = input()
left_fist = 0
right_fist = 0
face_passed = False

# 문자열의 왼쪽부터 탐색 반복
for act in action:
    # 얼굴의 일부('0')를 마주쳤을 경우 얼굴을 지나쳤음을 처리
    if act == '0':
        face_passed = True
    
    # 얼굴을 아직 지나치지 않은 상태에서 '@'를 찾은 경우
    if act == '@' and face_passed == False:
        left_fist += 1
        
    # 얼굴을 지나친 상태에서 '@'를 찾은 경우
    elif act == '@':
        right_fist += 1

print(left_fist, right_fist)
