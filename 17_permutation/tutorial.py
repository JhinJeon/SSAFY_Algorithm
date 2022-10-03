# 1. 원하는 개수 만큼 뽑기

sample_list = [1, 2, 3, 4, 5]
visited = [False] * 5
k = 2

answer = []     # append(list(arr))로 값을 추가할 리스트


def permutation_choice(arr):    # n 중 k개 뽑기, arr는 조건을 만족하는 경우 출력용
    global result
    # k개만큼 뽑은 경우
    if len(arr) == k:
        answer.append(list(arr))    # list()로 감싸야 얕은 복사가 돼서 현재 상태의 arr값 추가 가능
        return

    # 아직 충분한 개수가 아닌 경우
    for i in range(len(sample_list)):
        if not visited[i]:
            # 뽑으려는 인덱스 방문 처리 후 arr에 추가
            visited[i] = True
            arr.append(sample_list[i])

            # 재귀 호출
            permutation_choice(arr)

            # 이후 방문 여부 초기화
            arr.pop()
            visited[i] = False


permutation_choice(list())
print(answer)   # [[1, 2], [1, 3], [1,4], [1, 5], ...]

