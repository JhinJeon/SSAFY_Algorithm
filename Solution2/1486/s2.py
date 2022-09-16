# 장훈이의 높은 선반


# 조합 경우의 수를 도출하는 함수 combination
def combination(arr, k):
    result = []     # 조합 경우의 수 저장용
    if k > len(arr):
        return result

    if k == 1:      # 1개만 뽑는 경우
        for i in arr:
            result.append(i)      # 리스트에서 하나씩 뽑아서 추가

    elif k >= 1:    # 2개 이상 뽑아야 하는 경우
        # 앞쪽 범위 = 배열 앞쪽부터 k번째 수까지
        for i in range(len(arr) - k + 1):

            # 뒤쪽 범위 = 배열의 k+1번째부터 추가로 뽑기
            # 추가로 뽑는 개수는 k-1, k-2... 1개까지 경우의 수로 나뉨
            for j in combination(arr[i+1:], k - 1):
                result.append(arr[i] + j)

    return result


t = int(input())

for tc in range(1, t+1):
    n, b = map(int, input().split())            # n = 직원 수, b = 필요한 최소 높이
    workers = list(map(int,input().split()))    # 직원 키 리스트

    answer_case = list()                        # 정답에 부합하는 경우의 수 저장용
    for i in range(1, n+1):                     # 뽑기 경우의 수 : 1개부터 n개까지
        case = combination(workers, i)          # case = i개 뽑을 때 경우의 수
        
        # 함수에서 반환한 경우의 수들 중 조건에 부합하는 경우 answer_case에 추가
        for c in case:
            if c >= b:
                answer_case.append(c-b)

    # 높이 경우의 수 중 최솟값 출력
    answer = min(answer_case)
    print(f'#{tc}', answer)


