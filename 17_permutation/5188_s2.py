# 그리디 방식으로 해결
import sys
sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1, t+1):
    n = int(input())        # 이차원 배열의 가로, 세로 길이
    graph = [list(map(int, input().split())) for _ in range(n)]   # 이차원 배열 정보 입력받기
    value = graph[0][0]                                           # 시작 지점의 블록 값
    max_value = 10 * (n ** 2)                                     # 최솟값 도출 용도

    # 오른쪽 위~왼쪽 아래의 대각선 라인을 그어서 연산 수행
    # 라인은 오른쪽 아래 방향으로 이동
    # 오른쪽 아래를 왼쪽 위보다 먼저 계산하는 경우는 없으므로 순서대로 진행해도 무방
    k = 1                   # 라인 위치(열 인덱스 + 행 인덱스)
    finish = 2 * (n - 1)      # 최종 라인(가장 오른쪽 아래 칸의 열 인덱스 + 행 인덱스)
    while k <= finish:
        # 라인 시작 위치의 좌표(라인의 가장 오른쪽 위)
        col = 0 if k < n else k - n + 1
        row = k if k < n else n - 1
        while col < n and 0 <= row:
            # 현재 좌표의 블록이 테두리인 경우 왼쪽이나 위쪽 중 한쪽만 받도록 설정
            former_col = max_value
            former_row = max_value
            # 위쪽에 블록이 있는 경우 위쪽 블록 정보 가져오기
            if col > 0:
                former_col = graph[col-1][row]
            # 왼쪽에 블록이 있는 경우 왼쪽 블록 정보 가져오기
            if row > 0:
                former_row = graph[col][row-1]
            # 위쪽, 왼쪽 중 작은 값을 합산
            graph[col][row] += min(former_row, former_col)
            # 이후 왼쪽 아래 방향의 칸에도 적용
            col += 1
            row -= 1
        # 다음 라인으로 이동
        k += 1

    # 가장 오른쪽 아래 칸의 값 출력
    answer = graph[n-1][n-1]
    print(f'#{tc}', answer)
