# 이진탐색
# 발표할 코드
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

# 페이지 탐색 횟수를 반환하는 search_page 함수 정의
# front_page = 찾으려는 페이지 범위의 맨 처음 페이지
# last_page = 찾으려는 페이지 범위의 맨 마지막 페이지
# find_page = 찾으려는 페이지
# trial = 시도 횟수

def search_page(front_page, last_page, find_page, trial):
    front = front_page
    last = last_page
    trial += 1
    
    # mid = 첫 페이지와 마지막 페이지의 중간 페이지
    mid = int((front + last) / 2)
    
    # mid(중간 페이지)가 찾으려는 페이지와 일치하는 경우
    if mid == find_page:
        return trial
    
    # mid가 찾으려는 페이지보다 더 큰 경우
    elif mid > find_page:
        return search_page(front, mid, find_page, trial)
    
    # mid가 찾으려는 페이지보다 더 작은 경우
    else:
        return search_page(mid, last, find_page, trial)


for tc in range(1,t+1):
    # 책 페이지 수, a가 찾는 페이지, b가 찾는 페이지
    book, find_a, find_b = map(int,input().split())

    
    # 함수 결과를 a, b에 저장
    trial_a = search_page(1, book, find_a, 0)
    trial_b = search_page(1, book, find_b, 0)

    # a보다 b가 더 많은 시도를 한 경우(a가 더 빨리 찾은 경우)
    if trial_a < trial_b:
        answer = 'A'
    # a가 b보다 더 많은 시도를 한 경우(b가 더 빨리 찾은 경우)
    elif trial_a > trial_b:
        answer = 'B'
    # 탐색 시도 횟수가 동일한 경우
    else:
        answer = 0

    print(f'#{tc} {answer}')