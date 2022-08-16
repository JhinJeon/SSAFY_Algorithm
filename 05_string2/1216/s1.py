# 회문 검사 2
import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    # 한 줄로 구성된 입력값을 graph_vals로 받은 후 이를 10줄에 거쳐서 배분
    tc = int(input())

    graph = [list(input()) for _ in range(100)]
    answer_max = 0

    # 열 방향으로 회문 검사
    for col in range(100):
        for start_idx in range(100):
            for end_idx in range(start_idx, 100):
                # 열 방향 리스트의 일부를 pal_check 리스트로 분리한 후 회문 검사
                pal_check = graph[col][start_idx:end_idx+1]
                for i in range(len(pal_check)):
                    if pal_check[i] != pal_check[-1-i]:
                        break

                # 새로 발견한 회문의 길이가 이전에 발견된 회문의 최대 길이보다 긴 경우 값 갱신
                else:
                    answer = len(pal_check)
                    if answer > answer_max:
                        answer_max = answer

    # 행 방향으로 회문 검사
    for row in range(100):
        for start_idx in range(100):
            for end_idx in range(start_idx, 100):
                # 행 방향 값들의 일부를 pal_check 리스트에 담기
                pal_check = []
                for idx in range(start_idx,end_idx+1):
                    pal_check.append(graph[idx][row])

                # 회문 검사
                for i in range(len(pal_check)):
                    if pal_check[i] != pal_check[-1-i]:
                        break
                # 새로 발견한 회문의 길이가 이전에 발견된 회문의 최대 길이보다 긴 경우 값 갱신
                else:
                    answer = len(pal_check)
                    if answer > answer_max:
                        answer_max = answer

    print(f'#{tc} {answer_max}')