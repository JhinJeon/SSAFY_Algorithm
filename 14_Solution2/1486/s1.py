# 장훈이의 높은 선반
# 메모리 한도 초과

def combination(arr, k):
    result = []
    if k > len(arr):
        return result

    if k == 1:
        for i in arr:
            result.append([i])

    elif k >= 1:
        for i in range(len(arr) - k + 1):
            for j in combination(arr[i+1:], k - 1):
                result.append([arr[i]] + j)

    return result


t = int(input())

for tc in range(1, t+1):
    n, b = map(int, input().split())
    workers = list(map(int,input().split()))
    min_height = sum(workers)

    cases = list()
    for i in range(1, n+1):
        case = combination(workers, i)
        cases += case

    for c in cases:
        height = sum(c)
        if height > b and height < min_height:
            min_height = height

    print(f'#{tc}', min_height - b)


