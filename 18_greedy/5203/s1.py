# 베이비진 게임
import sys
sys.stdin = open('sample_input.txt')


# hand = 조합을 뽑을 대상 리스트
# case = 도출된 경우의 수
# arr = 경우의 수 저장용
# k = 인덱스 번호(탐색 범위 조절)
def combination(hand, case, arr, k):
    if len(arr) == 3:
        case.append(list(arr))
    for idx in range(k, len(hand)):
        arr.append(hand[idx])
        combination(hand, case, arr, idx + 1)
        arr.pop()


# arr = 길이가 3인 리스트(카드 3장 비교)
def is_babygin(arr):
    arr.sort(reverse=False)
    if arr[0] + arr[2] == 2 * arr[1] and arr[2] - arr[0] <= 2:
        return True


t = int(input())

for tc in range(1,t+1):
    deck = list(map(int,input().split()))
    player1 = []
    player2 = []
    answer = 0          # 반복문을 모두 수행하는 동안 answer 값이 안 바뀌면 무승부

    # 홀수 번째면 1p, 짝수 번째면 2p 카드 뽑기
    for i in range(len(deck)):
        if i % 2 == 0:
            player1.append(deck[i])

            # 1플레이어가 카드를 3장 이상 뽑은 경우
            if len(player1) >= 3:
                case_1 = []
                combination(player1, case_1, [], 0)     # 1P 손패에서 3개 뽑는 경우의 수
                for c1 in case_1:                       # 경우의 수들 중 baby_gin이 있는지 확인
                    if is_babygin(c1):
                        answer = 1
                        break
        else:
            player2.append(deck[i])
            # 2플레이어가 카드를 3장 이상 뽑은 경우
            if len(player2) >= 3:
                case_2 = []
                combination(player2, case_2, [], 0)     # 2P 손패에서 3개 뽑는 경우의 수
                for c2 in case_2:                       # 경우의 수들 중 baby_gin이 있는지 확인
                    if is_babygin(c2):
                        answer = 2
                        break
                        
        # 승부가 난 경우 반복문 즉시 종료
        if answer:
            break

    print(f'#{tc}', answer)