# 숫자 정렬(오름차순)
numbers = [3, 32, 29, 58, 2, 1, 69, 99, 74, 82]
answer = []
result = []
k = 3
visited = [False] * k


# 순열 뽑기(순서 고려 X)
def number_sort(array):
    if len(array) == k:
        answer.append(list(array))
        return

    for i in range(k):
        if not visited[i]:
            array.append(numbers[i])
            visited[i] = True

            number_sort(array)
            # 방문 여부 초기화
            visited[i] = False
            array.pop()


# 조합(순서 고려)
def combination(arr, idx):
    if len(arr) == k:
        result.append(list(arr))
        return
    for i in range(idx, len(numbers)):
        arr.append(numbers[i])
        combination(arr, idx + 1)

        arr.pop()


number_sort([])
combination([], 0)
print(answer)
print(result)
