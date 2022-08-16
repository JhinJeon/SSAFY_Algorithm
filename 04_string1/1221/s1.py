# SWEA - GNS
# 최초 작성 코드
import sys

sys.stdin = open('GNS_test_input.txt')

# words = 숫자에 대응하는 문자열 리스트
# numbers = words에 대응하는 숫자 리스트
words = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

t = int(input())

for tc in range(1, t + 1):
    # tc_no = 테스트 케이스 번호
    # n = 테스트 케이스 길이
    # letter_list = 문자열을 리스트로 입력받음
    tc_no, n = input().split()
    n = int(n)
    letter_list = list(input().split())

    # 문자열을 이에 대응하는 숫자로 전환
    for j in range(n):
        for i in range(10):
            if letter_list[j] == words[i]:
                letter_list[j] = numbers[i]

    # 숫자를 오름차순으로 정렬
    letter_list.sort(reverse=False)

    # 정렬된 숫자를 문자로 전환
    for j in range(n):
        for i in range(10):
            if letter_list[j] == numbers[i]:
                letter_list[j] = words[i]

    print(f'#{tc}')
    print(*letter_list)
