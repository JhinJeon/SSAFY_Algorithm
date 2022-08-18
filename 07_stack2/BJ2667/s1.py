# 단지번호붙이기
import sys
sys.stdin = open('input.txt')

def search_villiage(x,y):
    home = 0
    if x < 0 or x >= n or y < 0 or y >= n or graph[y][x] == '0':
        return home
    else:
        search_villiage(x-1,y)
        search_villiage(x,y-1)
        search_villiage(x+1,y)
        search_villiage(x,y+1)
        home += 1
    return home

n = int(input())

graph = [list(input()) for _ in range(n)]


for col in range(n):
    for row in range(n):
        result = search_villiage(row,col)
        if result > 0:
            print(result)


