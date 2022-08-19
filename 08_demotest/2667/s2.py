# 단지번호붙이기
# 최초로 작성한 버전(실행 속도 느림)
# 함수 정의할 때 인덱스 범위의 유효성과 상관없이 재귀 호출을 4번이나 하는 부분 때문에 느려지는 것 같다.

def search_villiage(x, y):
    # 유효하지 않은 인덱스 범위인 경우
    global wide
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0
    if graph[y][x] == '1':  # 1인 곳을 찾은 경우
        graph[y][x] = '0'   # 방문 처리(0으로 만들기)
        wide += 1
        search_villiage(x-1, y)
        search_villiage(x, y-1)
        search_villiage(x+1, y)
        search_villiage(x, y+1)  # (유효한 인덱스 범위 내에서) 0인 곳을 찾은 경우
    return 0

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