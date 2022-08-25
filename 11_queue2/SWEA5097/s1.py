# 회전

t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split()) # n = 리스트 길이, m = 로테이션 반복 횟수
    queue_list = list(map(int, input().split()))    # 큐 리스트
    queue_idx = m % n   # m을 n으로 나눈 나머지가 로테이션이 끝난 큐의 첫 번째 값을 가리키는 원본 큐의 인덱스 번호

    print(f'#{tc}', queue_list[queue_idx])