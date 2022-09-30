# 행성 터널

planet_count = int(input())

connection_info = [[] for _ in range(planet_count)]
for i in range(planet_count):
    x, y, z = map(int, input().split())
    connection_info[i]