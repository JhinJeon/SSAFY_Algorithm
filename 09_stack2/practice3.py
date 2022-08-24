# 부분집합 구하기

def get_subset(input_set, value_sum, depth):
    if value_sum == 10:
        print(input_set)
        return
    if depth == 10:
        if value_sum == 10:
            print(input_set)
            return  # return을 설정해야 똑같은 값이 여러 번 반복해서 출력되지 않음
    else:
        # 현재 원소를 뽑고 다음 재귀로 진행
        get_subset(input_set + [numbers[depth]], value_sum + numbers[depth], depth + 1)
        # 현재 원소를 뽑지 않고 다음 재귀로 진행
        get_subset(input_set, value_sum, depth + 1)

numbers = list(range(1,11))
get_subset([],0,0)