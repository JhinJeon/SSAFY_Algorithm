# 요리사
# 미완성
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
    choose = n // 2
    material_pool = [i for i in range(n)]
    answer = 20000

    combi = combination(material_pool, choose)      # 원소 n개 중에서 n//2개씩 들어간 조합
    pickcase = combination(combi,2)                 # 각 조합에서 묶음 한 쌍씩 선정
    
    for pick in pickcase:
        # 인덱스 중복이 있는지 확인
        if len(set(pick[0] + pick[1])) == n:
            # 중복되지 않는 묶음을 recipe_a, recipe_b로 나누기
            recipe_a = combination(pick[0], 2)
            recipe_b = combination(pick[1], 2)

            # 레시피 조합
            food_a = 0
            food_b = 0
            for ra in recipe_a:
                food_a += materials[ra[0]][ra[1]] + materials[ra[1]][ra[0]]
            for rb in recipe_b:
                food_b += materials[rb[0]][rb[1]] + materials[rb[1]][rb[0]]

            cook_result = food_a - food_b if food_a > food_b else food_b - food_a
            if cook_result < answer:
                answer = cook_result

    print(f'#{tc}', answer)