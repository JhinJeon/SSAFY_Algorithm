# 피자 굽기
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    n, m = map(int, input().split())    # n = 화덕 최대 용량, m = 구울 피자 수
    pizza = []  # 피자 번호와 치즈 양을 [인덱스 번호, 값]으로 받을 리스트
    for num, cheese in enumerate(list(map(int, input().split()))):
        pizza.append([num, cheese])
    oven = []   # 화덕에 굽는 피자 리스트(큐)

    while len(oven) > 1: # 조리 중인 피자 수가 1개 이하가 될 때까지 반복
        while len(oven) < n and pizza:  # 화덕에 빈 공간이 남고 구울 피자가 남아 있는 경우
            oven.append(pizza.pop(0))   # 화덕에 새 피자 추가
        while True:
            cheese_melt = oven.pop(0)   # [피자 번호, 치즈량]을 받은 뒤 치즈량을 절반(버림)으로 변경
            cheese_melt[1] = cheese_melt[1] // 2
            if cheese_melt[1] == 0:     # 치즈가 다 녹아서 없어지는 경우 반복문 종료
                break
            oven.append(cheese_melt)    # 이상 없는 경우 화덕 돌리기

    answer = oven[-1][0] + 1
    print(f'#{tc}', answer)    # 피자 번호 출력
