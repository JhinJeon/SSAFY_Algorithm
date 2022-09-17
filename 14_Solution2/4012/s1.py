# 요리사

import sys
sys.stdin = open('sample_input.txt')


def combination(arr, k):
    result = []     # 조합 경우의 수 저장용
    if k > len(arr):
        return result

    if k == 1:      # 1개만 뽑는 경우
        for i in arr:
            result.append([i])      # 리스트에서 하나씩 뽑아서 추가

    elif k >= 1:    # 2개 이상 뽑아야 하는 경우
        # 앞쪽 범위 = 배열 앞쪽부터 k번째 수까지
        for i in range(len(arr) - k + 1):

            # 뒤쪽 범위 = 배열의 k+1번째부터 추가로 뽑기
            # 추가로 뽑는 개수는 k-1, k-2... 1개까지 경우의 수로 나뉨
            for j in combination(arr[i+1:], k - 1):
                result.append([arr[i]] + j)

    return result


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    materials = [list(map(int,input().split())) for _ in range(n)]
    choose = n // 2                                 # 배열에서 한 번에 선택할 인자 수
    material_pool = [i for i in range(n)]           # 이차원 배열 그래프
    answer = 20000                                  # 정답(최대 20000)

    combi = combination(material_pool, choose)      # 원소 n개 중에서 n//2개씩 들어간 조합
    
    for case_a in combi:     # 조합 경우의 수에서 하나씩 반환
        # 요리(재료 시너지) 결과
        food_a = 0
        food_b = 0

        # 요리 A의 맛 구하기
        for ra in combination(case_a, 2):
            food_a += materials[ra[0]][ra[1]] + materials[ra[1]][ra[0]]

        case_b = list(set(range(n)) - set(case_a))      # 중복되는 경우의 수 제외

        # 요리 B의 맛 구하기
        for rb in combination(case_b, 2):
            food_b += materials[rb[0]][rb[1]] + materials[rb[1]][rb[0]]

        # 요리 a와 요리 b의 차이 구하기(절댓값)
        cook_result = food_a - food_b if food_a > food_b else food_b - food_a

        # 최솟값을 경신하는 경우 answer 값 변경
        if cook_result < answer:
            answer = cook_result

    print(f'#{tc}', answer)