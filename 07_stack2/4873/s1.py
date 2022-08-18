# 반복문자 지우기


def zip(string):
    answer = ''
    dup_check = [[] for _ in range(len(string))]
    for s in string:
        dup_check.append(s)
        


t = int(input())

for tc in range(1, t + 1):
    strings = input()
    answer = ''
