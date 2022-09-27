# 동철이의 일 분배
import sys
sys.stdin = open('input.txt')


def work_tree(work_no, process):
    global answer

    # 최댓값 경신 여지가 없는 경우 백트래킹
    if answer > process:
        return
    
    # 모든 직원이 한 번씩 일한 경우
    if False not in worker_put:
        # 최댓값 경신인 경우 해당 값으로 대체
        if answer < process:
            answer = process
            
    # 가장 능률이 좋은 직원을 max_value에 저장
    max_value = 0
    max_idx = 0
    for k in range(n):
        case_value = workers[work_no][k] / 100
        if not worker_put[k] and max_value < case_value:
            max_value = case_value
            max_idx = k

    # process에 max_value 곱하기
    process *= max_value
    
    # 직원 노동 처리
    worker_put[max_idx] = True
    
    # 다음 번호로 이동
    work_no = (work_no + 1) % n
    work_tree(work_no, process)


t = int(input())

for tc in range(1,t+1):
    n = int(input())    # 일의 개수
    workers = []        # 작업자의 능률 정보
    answer = 0
    for i in range(n):
        workers.append(list(map(int,input().split())))      # n번째 일을 담당할 때 성공 확률

    for i in range(n):
        worker_put = [False] * n  # 직원 동원 여부
        work_tree(i, 1)

    print(f'#{tc}', answer)
