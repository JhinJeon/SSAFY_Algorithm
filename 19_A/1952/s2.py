# 수영장
# 3달 요금 < 1달 요금인 케이스에 대응 불가
import sys
sys.stdin = open('debug_input.txt')


# 한달(또는 일) 단위와 3개월권 중에 저렴한 것을 골라주는 함수 dfs
def dfs(k, case_sum):
    global fee_sum
    # start = 탐색 시점 이전까지의 월 단위 요금 합계
    # case_sum = 3개월 단위/1개월 단위 중 더 저렴한 경우를 고른 요금의 합계
    if k < 12:
        calculated[k] = True
        case_sum += fee_plan[k]

    # 12달 요금을 모두 계산한 경우
    if k >= 12 and False not in calculated:
        result = start + case_sum
        if fee_sum > result:
            fee_sum = result
        return
    
    # 현 시점에서 앞으로 3개월 간 요금과 3개월 이용권 요금 비교
    for i in range(k, 12):
        # 이전 시점에 계산 안 한 경우가 있는 경우 return(백트래킹)
        three = sum(fee_plan[i:i+3])    # 3달치 요금(1개월 * 3)
        if three:                       # 앞으로 3달 간(현재 달 포함) 수영 계획이 있는 경우
            if three > quarter:             # 3개월 이용권이 더 싼 경우
                for j in range(i, i+3):
                    if j < 12:              # 인덱스 범위를 벗어나지 않도록
                        calculated[j] = True
                # 재귀 호출
                dfs(i+3, case_sum + quarter - fee_plan[k])
                # 이후 원상복귀
                for j in range(i, i+3):
                    if j < 12:  # 인덱스 범위를 벗어나지 않도록
                        calculated[j] = False
            else:
                dfs(i + 1, case_sum)
                if i < 11:
                    calculated[i] = False
                
        # 이용 계획이 없는 경우 일단 계산함 처리
        else:
            calculated[i] = True

    # 12달 요금을 모두 계산한 경우(1년 내내 이용 계획이 있는 경우)
    else:
        result = start + case_sum
        if fee_sum > result and False not in calculated:
            fee_sum = result
        return


t = int(input())

for tc in range(1, t+1):
    # 수영장 요금(1일, 1주, 3달, 1년)
    daily, monthly, quarter, annual = map(int, input().split())

    fee_sum = max(daily, monthly, quarter, annual) * 12     # 수영장 이용에 필요한 최소 요금
    # 월별 수영장 이용 횟수
    monthly_plan = list(map(int, input().split()))
    fee_plan = [0] * 12

    # 매 달마다 일일권을 일자만큼 사는 것과 월 이용권을 사는 것 중 더 싼 값으로 대체
    for m in range(12):
        playtime = monthly_plan[m]
        daily_fee = daily * playtime
        if playtime and daily_fee > monthly:
            fee_plan[m] = monthly
        else:
            fee_plan[m] = daily_fee

    # 1달 + 3달 조합으로 최적의 요금 도출
    for i in range(12):
        calculated = [False] * 12   # 모두 계산되었는지 확인하는 용도
        for k in range(i):
            calculated[k] = True
        start = sum(fee_plan[:i])
        dfs(i, 0)

    # 1년치로 끊는 게 더 싼 경우
    answer = min(fee_sum, annual)

    print(f'#{tc}', answer)

