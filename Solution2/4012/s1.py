# 요리사
import sys
sys.stdin = open('debug_input.txt')


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
    cook_result = list()
    choose = n // 2
    material_pool = [i for i in range(n)]
    combi = combination(material_pool, choose)

    combi_cases = len(combi)
    for ca in range(combi_cases-1):
        for cb in range(ca+1, combi_cases):
            
            # 인덱스 중복이 있는지 확인
            if len(set(combi_cases[ca] + combi_cases[cb])) == n:
                recipe_a = combination(combi_cases[ca],2)
                recipe_b = combination(combi_cases[cb],2)

                # 레시피 조합
                food_a = 0
                food_b = 0
                for ra in recipe_a:
                    for rb in recipe_b:
                        food_a += materials[ra[0]][ra[1]] + materials[ra[1]][ra[0]]
                        food_b += materials[rb[0]][rb[1]] + materials[rb[1]][rb[0]]
                cook_result.append(abs(food_a - food_b))

    answer = min(cook_result)
    print(f'#{tc}', answer)