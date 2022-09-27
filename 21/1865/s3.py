# 동철이의 일 분배
# 디버그용
# 중복되는 경우를 해결해야 함

import sys
sys.stdin = open('input.txt')


t = int(input())

for tc in range(1,t+1):
    n = int(input())    # 일의 개수
    workers = []        # 작업자의 능률 정보
    job_finished = [False] * n      # 일을 마쳤는지 확인
    worker_put = [False] * n        # 직원이 일을 했는지 확인
    for i in range(n):
        workers.append(list(map(int,input().split())))      # n번째 일을 담당할 때 성공 확률

    process = 100
    # 모든 직원이 일을 한 개씩 할 때까지 반복
    while False not in worker_put and False not in job_finished:
        # 가장 능률이 좋은 직원을 max_value에 저장
        max_value = 0
        for col in range(n):
            # 아직 하지 않은 일 탐색
            if not job_finished[col]:
                for row in range(n):
                    # 아직 일하지 않은 직원 탐색
                    if not worker_put[row]:
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

    print(f'#{tc}', ':%10.6f'%round(process, 6))
