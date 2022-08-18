# 회문 검사 2
# 팰린드롬 검사하는 부분 변경

import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    # 한 줄로 구성된 입력값을 graph_vals로 받은 후 이를 100줄에 거쳐서 배분
    tc = int(input())

    graph = [list(input()) for _ in range(100)]
    answer_max = 0

    # 열 방향으로 회문 검사
    for col in range(100):
        # 각 열마다 회문 탐색
        # start_idx = 탐색 시작 범위 인덱스
        # end_idx = 탐색 끝 범위 인덱스
        for start_idx in range(100):
            for end_idx in range(99, start_idx-1, -1):
                # 열 방향 리스트의 일부를 pal_check 리스트로 분리한 후 회문 검사
                pal_check = graph[col][start_idx:end_idx+1]
                if pal_check == pal_check[::-1]:
                    answer = len(pal_check)
                    break
            if answer > answer_max:
                answer_max = answer


    # 행 방향으로 회문 검사
    for row in range(100):
        # 각 행마다 회문 탐색
        # start_idx = 탐색 시작 범위 인덱스
        # end_idx = 탐색 끝 범위 인덱스
        for start_idx in range(100):
            for end_idx in range(99, start_idx-1, -1):
                # 행 방향 값들의 일부를 pal_check 리스트에 담기
                pal_check = []
                for idx in range(start_idx,end_idx+1):
                    pal_check.append(graph[idx][row])

                # 회문 검사
                if pal_check == pal_check[::-1]:
                    answer = len(pal_check)
                    break
            if answer > answer_max:
                answer_max = answer


    print(f'#{tc} {answer_max}')