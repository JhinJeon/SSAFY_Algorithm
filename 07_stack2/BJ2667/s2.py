# 단지번호붙이기
# 재귀함수는 구현 불가? : 방문 완료 처리를 하지 않으면 재귀 호출이 지나치게 깊어지는 문제가 있음

import sys
sys.stdin = open('input.txt')


def search_villiage(x, y):
    global wide     # wide = 1의 개수를 계산하는 전역 변수(매 행,열을 기준으로 탐색할 때마다 값 초기화)
    if x < 0 or x >= n or y < 0 or y >= n:  # 유효하지 않은 인덱스 범위인 경우
        return 0
    if graph[y][x] == '1':  # 1인 곳을 찾은 경우
        graph[y][x] = '0'   # 방문 처리(0으로 만들기)
        wide += 1
        # 이하 인접한 노드 탐색
        search_villiage(x-1, y)
        search_villiage(x, y-1)
        search_villiage(x+1, y)
        search_villiage(x, y+1)
    return 0    # (유효한 인덱스 범위 내에서) 0인 곳을 찾은 경우

n = int(input())

graph = [list(input()) for _ in range(n)]

answer = []
for col in range(n):
    for row in range(n):
        wide = 0
        search_villiage(row, col)
        if wide > 0:    # 넓이가 1 이상 감지되는 경우 answer 리스트에 추가
            answer.append(wide)

# 오름차순 정렬
answer.sort(reverse=False)

print(len(answer))
for a in answer:
    print(a)
