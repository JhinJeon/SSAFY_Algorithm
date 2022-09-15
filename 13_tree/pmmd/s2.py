# 사칙연산
import sys
sys.stdin = open('input.txt')


# 트리에서 루트로 수렴하는 사칙 연산을 수행하는 함수 calculate
def calculate(k):
    val = value[k]      # 현재 노드 번호에 저장된 값 확인
    if not val:         # 현재 노드에 값이 저장되지 않은경우(사칙연산 기호가 저장된 경우)
        
        # 왼쪽 노드와 오른쪽 노드에서 값 가져오기
        calculate(left_child[k])
        calculate(right_child[k])
        
        # 노드에 저장된 연산자 부호에 따라 연산 실행
        if calculators[k] == '+':
            result = value[k] = value[left_child[k]] + value[right_child[k]]
        elif calculators[k] == '-':
            result = value[k] = value[left_child[k]] - value[right_child[k]]
        elif calculators[k] == '*':
            result = value[k] = value[left_child[k]] * value[right_child[k]]
        elif calculators[k] == '/':
            result = value[k] = value[left_child[k]] / value[right_child[k]]
        return result
    
    else:               # 현재 노드에 값이 저장되어 있는 경우 값 반환
        return value[k]


for tc in range(1,11):
    n = int(input())
    # 순서대로 왼쪽 자식, 오른쪽 자식
    left_child = [0] * (n+1)
    right_child = [0] * (n+1)

    # value와 calculators는 동일한 인덱스 번호에 모두 값이 있으면 안 됨(연산기호나 숫자 중 하나만)
    value = [0] * (n + 1)           # 값 저장
    calculators = [""] * (n+1)      # 사칙연산 기호 저장

    for _ in range(n):
        info_input = list(input().split())      # 노드 정보 임시 저장
        idx = int(info_input[0])                # idx = 노드 번호
        if len(info_input) == 4:                # 사칙연산 부호와 왼쪽 자식, 오른쪽 자식을 추가로 입력받는 경우
            left_child[idx] = int(info_input[2])
            right_child[idx] = int(info_input[3])
            calculators[idx] = info_input[1]    # 사칙연산 기호는 calculators에 저장
        else:
            value[idx] = int(info_input[1])     # 값은 value에 저장

    # 루트 노드부터 탐색 시작
    answer = int(calculate(1))

    print(f'#{tc}', answer)