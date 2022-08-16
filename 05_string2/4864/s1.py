# 문자열 비교
import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):

    # search_range = str1이 str2 안에 들어있는지 확인하기 위한 인덱스 기준
    # slicing_range = 문자열 슬라이싱 기준 인덱스
    str1 = input()
    str2 = input()
    search_range = len(str1)
    slicing_range = len(str2) - len(str1)

    for idx in range(slicing_range+1):
        # str2 내에 str1을 찾았으면 즉시 반복문 종료
        if str2[idx:idx+search_range] == str1:
            answer = 1
            break
    # str2 내에 str1을 찾지 못한 경우
    else:
        answer = 0

    print(f'#{tc} {answer}')