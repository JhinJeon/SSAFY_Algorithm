# 회문
import sys
sys.stdin = open('sample_input.txt')


t = int(input())

for tc in range(1, t + 1):
    # answer = 회문을 찾은 경우 저장해서 출력하기 위한 임시 변수
    n, m = map(int, input().split())
    graph = [list(input()) for _ in range(n)]
    answer = ''
    
    # 열 방향으로 회문 검사
    for col in range(n):
        for start_idx in range(n - m + 1):
            for row in range(m):
                # 탐색 범위의 앞뒤가 다른 경우 반복문 종료
                # 그래프 끝 범위를 -row -1 -start_idx로 설정하면 반복문이 진행될수록 탐색 범위가 좁아짐
                if graph[col][row + start_idx] != graph[col][-row - 1 - (n-m-start_idx)]:
                    break
            # 탐색 범위 내의 모든 문자들의 앞뒤가 같으면 묶어서 answer에 추가
            else:
                answer = ''.join(graph[col][start_idx: start_idx + m])

    # 행 방향으로 회문 검사
    for row in range(n):
        for start_idx in range(n - m + 1):
            for col in range(m):
                # 탐색 범위의 앞뒤가 다른 경우 반복문 종료
                if graph[col + start_idx][row] != graph[-col - 1 - (n-m-start_idx)][row]:
                    break
            # 탐색 범위 내의 모든 문자들의 앞뒤가 같으면 묶어서 answer에 추가
            else:
                for col_idx in range(start_idx, start_idx + m):
                    answer += graph[col_idx][row]

    print(f'#{tc} {answer}')
