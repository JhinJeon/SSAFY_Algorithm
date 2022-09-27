# 병합 정렬
import sys

sys.stdin = open('sample_input.txt')


# 병합 정렬을 위해 개별 집합 단위로 분리
def divide(arr):
    # 길이가 1 단위까지 분리된 경우
    if len(arr) == 1:
        return arr
    std = len(arr) // 2     # 분리 기준
    left = arr[:std]        # 왼쪽 부분
    right = arr[std:]       # 오른쪽 부분
    return merge(divide(left), divide(right))


# 분리한 집합을 병합하는 함수
def merge(l, r):
    global case
    result = []     # 병합 정렬 결과
    if l and r and l[-1] > r[-1]:
        case += 1

    i, j = 0, 0
    # 작은 수부터 정렬
    while len(l) > i and len(r) > j:
        # 작은 수를 병합 정렬에 추가한 후 인덱스 범위 이동
        if l[i] < r[j] :
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
            
    # 정렬되지 않은 부분 마저 정렬
    result += l[i:]
    result += r[j:]

    # 결과 반환
    return result


t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    array = list(map(int, input().split()))
    standard = n // 2
    is_sort = False  # 정렬 여부 확인용
    case = 0  # 왼쪽 원소 마지막 > 오른쪽 원소 마지막인 경우의 수
    answer = divide(array)[standard]

    print(f'#{tc}', answer, case)
