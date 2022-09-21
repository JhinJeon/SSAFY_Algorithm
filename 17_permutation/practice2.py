# baby gin
import sys
sys.stdin = open('input.txt')

# 조합 경우의 수를 반환하는 함수 array
def combination(arr, k):
    arr.append(decklist[k])     # 현재 인덱스 번호에서 1개 뽑기
    if len(arr) == 3:   # 3개를 뽑은 경우
        case.append(list(arr))  # 경우의 수에 추가하고 탐색 종료
        return

    # 아직 3개를 뽑지 않은 경우
    for i in range(k+1, len(decklist)):
        # 뒤쪽의 인덱스에서 경우의 수 찾기(재귀호출)
        combination(arr, i)

        # 탐색 과정 되돌리기
        arr.pop()


# baby gin 존재 여부를 확인하는 함수 ginger
def ginger(array):
    array.sort(reverse=False)   # 오름차순으로 정렬
    left_num = int(array[0])    # 가장 작은 수
    center_num = int(array[1])  # 중간 수
    right_num = int(array[2])   # 가장 큰 수

    if (left_num + right_num) // 2 == center_num:   # 평균이 중간 수와 일치하는 경우
        # 연속으로 이어지거나 셋 다 동일한 수인지 확인
        gap = right_num - left_num
        if gap == 0 or gap == 2:    # 두 조건 다 만족하면 True 반환
            return True


t = int(input())

for tc in range(1, t+1):
    decklist = list(input())
    case = []
    answer = False      # baby_gin 체크용(기본값 = 거짓)

    combination([], 0)

    for c in case:
        hand_1 = c  # 3장 뽑은 핸드 1
        hand_2 = decklist.copy()    # 핸드 1에 있는 숫자를 제외한 3장을 뽑은 핸드 2
        for h in hand_1:    # 핸드 1에 포함된 숫자 제외
            hand_2.remove(h)

        # baby_gin에 해당하는 조합이 발견되는 경우 True로 전환
        if ginger(hand_1) and ginger(hand_2):
            answer = True
            break

    print(f'#{tc}', answer)
