# 순열
# dfs와 유사

numbers = list(range(1,5))
visited = [False] * 4
length = 3


def permutations(arr):  # arr = 경우의 수가 담긴 리스트
    if len(arr) == length:
        print(arr)
        return

    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            arr.append(numbers[i])
            
            # 재귀호출
            permutations(arr)
            
            # 재귀함수 종료 후
            visited[i] = False  # visited 기록 초기화
            arr.pop()   # 잘못된 경로로 가는 경우 마지막 분기까지 경로 취소하기 위함

# 순서에 따라 정렬 - 앞뒤가 바뀐 값도 별개의 값으로 출력
permutations([])