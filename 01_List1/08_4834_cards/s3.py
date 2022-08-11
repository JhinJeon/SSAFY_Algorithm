import sys
sys.stdin = open("sample_input.txt")

# t = 테스트 케이스 횟수
t = int(input())

for tc in range(1,t+1):
    # n = 카드 수
    n = int(input())
    # cards = 카드에 적힌 숫자(n개)
    cards = input()
    # num_count = 카드에 어떤 숫자가 몇 번 적혔는지 세는 용도
    num_count = [0] * 10
    for card in cards:
        num_count[int(card)] += 1

    # 가장 자주 나온 숫자 카운트
    most_frequent = num_count[0]
    most_frequent_idx = 0
    # 0 이외의 다른 숫자가 더 자주 나온다면 해당 숫자로 대체
    # 만약 빈도 수가 같다면 더 큰 수로 대체
    for i in range(1,10):
        if num_count[i] >= most_frequent:
            most_frequent = num_count[i]
            most_frequent_idx = i

    print(f'#{tc} {most_frequent_idx} {most_frequent}')