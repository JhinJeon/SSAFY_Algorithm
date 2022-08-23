# 조합 2

def combinations(arr, depth):
    # 최대 깊이에 도달했을 경우
    if depth == len(numbers):
        # 뽑고 싶은 개수만큼 있는 경우에만 출력
        if len(arr) == length:
            print(arr)
        return

    # 현재 원소를 뽑는 경우
    combinations(arr + [numbers[depth]], depth + 1)
    
    # 현재 원소를 뽑지 않는 경우
    combinations(arr, depth + 1)

numbers = [1,2,3,4]
length = 3

combinations([], 0)