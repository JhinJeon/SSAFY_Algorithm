import sys
sys.setrecursionlimit(100000000)

# 차례대로 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]    
answer = []

def solution(places):
    # places = 5 * 5의 이차원 배열
    # p = 응시자가 앉아있는 자리
    # o = 빈 테이블
    # x = 파티션(공간 분리)
    
    
    visited = [[False] * 5 for _ in range(5)]
    
    for place in places:
        graph = []
        is_invalid = False
        for p in place:
            graph.append(list(p))

        for col in range(5):
            for row in range(5):
                if graph[col][row] == 'P':
                    for direction in range(4):
                        nx = row + dx[direction]
                        ny = col + dy[direction]
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if graph[ny][nx] == 'X':
                                continue
                            elif graph[ny][nx] == 'P':
                                is_invalid = True
                            else:
                                for direction2 in range(4):
                                    nx2 = nx + dx[direction2]
                                    ny2 = ny + dy[direction2]
                                    if 0 <= nx2 < 5 and 0 <= ny2 < 5 and direction != ((direction2 + 2) % 4):
                                        if graph[ny2][nx2] == 'P':
                                            is_invalid = True
                                    
            
                            
        if is_invalid:
            answer.append(0)
        else:
            answer.append(1)
            
    return answer