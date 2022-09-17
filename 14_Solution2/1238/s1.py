#  contact
# BFS로 풀어야 함(DFS로 해결한 방식)

import sys
sys.stdin = open('input.txt')


# 발신자와 수신자를 연결하는 contact 함수
def contact(k):
    global max_no
    received[k] = True
    if k > max_no:
        max_no = k
    for n in connection_info[k]:
        if n != 0 and not received[n]:
            contact(n)


for tc in range(1,11):
    data_length, starting_point = map(int,input().split())
    input_info = list(map(int,input().split()))        # 2개 단위로 (발신, 수신)
    connection_info = [[0] for _ in range(101)]
    received = [False] * 101            # 수신 여부(최대 100명)
    max_no = 0                          # 수신자 중 가장 큰 번호
    for i in range(0, data_length, 2):
        connection_info[input_info[i]].append(input_info[i+1])

    contact(starting_point)

    print(f'#{tc}', max_no)