calculate = {                                   # 연산 수행
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
}


def lvr(n):
    if ch1[n] and ch2[n]:                       # 해당 노드의 자식이 있다면
        L = lvr(ch1[n])                         # 왼쪽 자식 노드
        R = lvr(ch2[n])                         # 오른쪽 자식 노드
        return calculate[node_info[n]](L, R)    # 재귀를 통해 사칙연산 계산

    else:                                       # 해당 노드의 자식이 없다면
        return node_info[n]                     # 자기 자신의 숫자 반환


for tc in range(1, 11):
    N = int(input())

    node_info = [""] * (N + 1)                  # 자기 자신의 값 저장(숫자 또는 연산자)
    ch1 = [0] * (N + 1)                         # 왼쪽 자식
    ch2 = [0] * (N + 1)                         # 오른쪽 자식

    for i in range(N):
        arr = input().split()
        idx = int(arr[0])                       # 정점 번호
        if len(arr) == 2:                       # 받아온 정보의 길이가 2이면(숫자)
            node_info[idx] = int(arr[1])        # node_info에 저장
        else:                                   # 받아온 정보의 길이가 4이면(연산자)
            node_info[idx] = arr[1]             # node_info에 저장
            ch1[idx] = int(arr[2])              # 왼쪽 자식 인덱스 저장
            ch2[idx] = int(arr[3])              # 오른쪽 자식 인덱스 저장

    print(f"#{tc} {int(lvr(1))}")               # 중위순회 실행 및 return 값 출력