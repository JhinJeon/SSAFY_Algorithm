# 동철이의 일 분배
import sys
sys.stdin = open('input.txt')


def work_tree(idx):
    global process, answer
    for _ in range(n):
        # 최댓값 경신 여지가 없는 경우 백트래킹
        if answer > process:
            break

        # 가장 능률이 좋은 직원을 max_value에 저장
        max_value = 0
        for col in range(n):
            # 아직 하지 않은 일 탐색
            if not worker_put[col]:
                for row in range(n):
                    # 아직 일하지 않은 직원 탐색
                    if not job_finished[row]:
                        # 직원의 능률 조회
                        case_value = workers[col][row] / 100
                        # 최댓값을 max_value에 저장
                        if max_value < case_value:
                            max_value = case_value
                            # max_value에 해당하는 col과 row 저장
                            job_idx = col
                            worker_idx = row

        # process에 max_value 곱하기
        process *= max_value

        # 직원 노동 처리
        job_finished[job_idx] = True
        worker_put[worker_idx] = True

    # 모든 직원이 한 번씩 일한 이후 - 최댓값 경신인 경우 해당 값으로 대체
    if answer < process:
        answer = process


t = int(input())

for tc in range(1,t+1):
    n = int(input())    # 일의 개수
    workers = []        # 작업자의 능률 정보
    answer = 0
    job_finished = [False] * n
    worker_put = [False] * n
    for i in range(n):
        workers.append(list(map(int,input().split())))      # n번째 일을 담당할 때 성공 확률

    for j in range(n):
        process = 100
        work_tree(j)

    print(f'#{tc}', ':%10.6f'%round(answer, 6))
