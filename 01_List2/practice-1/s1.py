# 배결 간 절대값의 합 구하기

import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    # 그래프(이중 리스트) 구축
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    # 행(열) 인덱스 범위를 벗어나는 경우 계산하지 않고, 유효한 인덱스 범위인 경우 절댓값 계산
    for col in range(n):
        for row in range(n):
            # 열 인덱스가 0보다 작아지는 경우(왼쪽 이탈)
            if col - 1 < 0:
                pass
            else:
                answer += abs(graph[col][row] - graph[col-1][row])
            # 열 인덱스가 n 이상이 되는 경우(오른쪽 이탈)
            if col + 1 >= n:
                pass
            else:
                answer += abs(graph[col][row] - graph[col + 1][row])
            # 행 인덱스가 n 이상이 되는경우(아래쪽 이탈)
            if row + 1 >= n:
                pass
            else:
                answer += abs(graph[col][row] - graph[col][row + 1])
            # 행 인덱스가 0보다 작아지는 경우(위쪽 이탈)
            if row - 1 < 0:
                pass
            else:
                answer += abs(graph[col][row] - graph[col][row - 1])

    print(f'#{tc} {answer}')
