#  contact
# BFS

import sys
sys.stdin = open('input.txt')


# 발신자와 수신자를 연결하는 contact 함수
def contact(k):
    global max_no
    received[k] = True                      # 수신 여부 확인
    search_queue = [k]                      # 현재 위치 기록
    while True:
        last_leaf = search_queue.copy()     # last_leaf = 현재 통신 가능한 인원 번호를 박제해 둔 리스트
        for _ in range(len(search_queue)):
            v = search_queue.pop(0)  # 현재 정점
            for next_v in connection_info[v]:  # 현재 정점과 인접한 모든 정점에 대해
                if next_v != 0 and not received[next_v]:  # 아직 방문하지 않았다면
                    received[next_v] = True  # 인접 정점 방문처리
                    search_queue.append(next_v)  # 인접 정점을 큐에 삽입
                    
        # 더 이상 연락할 사람이 없는 경우(마지막 주자인 경우)
        if not search_queue:
            return last_leaf
            break


for tc in range(1,11):
    data_length, starting_point = map(int,input().split())  # 입력받는 값 임시 저장
    input_info = list(map(int,input().split()))        # 2개 단위로 (발신, 수신)
    connection_info = [[0] for _ in range(101)]        # 연결 정보 기록(인덱스 번호 : 발신자, 값 : 수신자)
    received = [False] * 101                           # 수신 여부(최대 100명)
    max_no = starting_point                            # 수신자 중 가장 큰 번호

    # 입력받은 값을 연결 정보에 기록
    for i in range(0, data_length, 2):
        connection_info[input_info[i]].append(input_info[i+1])

    answer = max(contact(starting_point))   # 마지막 주자들 중 최댓값 번호 반환

    print(f'#{tc}', answer)