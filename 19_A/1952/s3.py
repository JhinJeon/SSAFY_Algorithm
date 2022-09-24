# 수영장
# dfs + 3달 요금이 1달 요금보다 저렴한 테스트케이스 대응용

import sys
sys.stdin = open('sample_input.txt')


# 모든 경우의 수를 탐색한 뒤 가장 저렴한 요금을 반환하는 함수 dfs
def dfs(k, case_sum):       # k = 깊이(월), case_sum = 요금
    global fee_sum

    # 12달 요금을 모두 계산한 경우
    if k >= 12:
        if fee_sum > case_sum:
            fee_sum = case_sum
        return
    
    # 현 시점 기준 일일 요금, 월 이용권, 3개월 이용권 요금 비교
    if monthly_plan[k]:
        dfs(k+1, case_sum + monthly_plan[k] * daily)
        dfs(k + 1, case_sum + monthly)
        dfs(k + 3, case_sum + quarter)
    # 수영 계획이 없는 경우 다음 달로 넘어가기
    else:
        dfs(k+1, case_sum)


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
    dfs(0, 0)

    # 1년치로 끊는 게 더 싼 경우
    answer = min(fee_sum, annual)

    print(f'#{tc}', answer)

