# 이진 탐색 함수 binary_search
def binary_search(x):
    s, e = 0, n - 1     # 정렬 기준(맨 처음과 맨 끝)
    check = 0
    while s <= e:       # 기준이 정방향으로 되어 있는 경우
        mid = (s + e) // 2      # 분리 기준 인덱스
        # s와 mid가 일치하는 경우 True 반환(+1)
        if a[mid] == x:
            return True
        # x가 큰 쪽 가지에 있는 경우
        elif a[mid] > x:
            # 또 큰 쪽에 있는 경우 탐색 중단
            if check == 1:
                break
            check = 1
            e = mid - 1    # 탐색 범위 축소
        # x가 작은 쪽 가지에 있는 경우
        else:
            # 또 작은 쪽에 있는 경우 탐색 중단
            if check == 2:
                break
            check = 2
            s = mid + 1     # 탐색 범위 축소
    return False


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()        # a 리스트 정렬
    total = 0
    # 리스트 b의 숫자를 하나씩 대조하며 조건에 맞는 케이스 합산
    for num in b:
        total += binary_search(num)
    print(f'#{tc} {total}')