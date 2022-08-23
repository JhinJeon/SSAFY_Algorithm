# 최소 생산 비용

import sys
sys.stdin = open('sample_input.txt')


# 생산비용의 최솟값을 구하는 permutation 함수 정의
def permutation(col_count, value):  # col_count = 행 깊이, value = 생산 비용
    global result   # result = 생산비용의 최솟값 저장
    if col_count == n:  # 모든 행을 탐색했을 경우
        if value < result:  # 새로운 최솟값을 경신하는 경우
            result = value
        return
    
    for i in range(n):  # 새로운 범위 탐색
        if not visited[i]:  # 기존에 탐색하지 않은 열이라면
            value += factory[col_count][i]  # 탐색 처리 및 해당 좌표의 값을 value에 가산
            visited[i] = True

            # 이미 기존의 최솟값을 초과하는 경우 탐색 중단(백트래킹)
            if value <= result:
                permutation(col_count + 1, value)

            # 탐색 정보, 값을 이전 단계로 되돌리기
            value -= factory[col_count][i]
            visited[i] = False


t = int(input())

for tc in range(1,t+1):
    n = int(input())
    factory = [list(map(int,input().split())) for _ in range(n)]    # 품목별 생산 비용 입력
    visited = [False] * n   # 방문 여부 표시
    result = 99 * n # 기본 최솟값(공장 별 최댓값은 99)

    permutation(0, 0)


    print(f'#{tc}', result)

