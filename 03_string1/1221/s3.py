# SWEA - GNS
# 버블 정렬 개선된 버전
import sys
sys.stdin = open('GNS_test_input.txt')
# words = 숫자에 대응하는 문자열 리스트
words = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

t = int(input())

for tc in range(1, t + 1):
    # tc_no = 테스트 케이스 번호
    # n = 테스트 케이스 길이
    # letter_list = 문자열을 리스트로 입력받음
    tc_no, n = input().split()
    n = int(n)
    letter_list = list(input().split())

    # 문자를 이에 대응하는 숫자로 전환
    for j in range(n):
        for idx, val in enumerate(words):
            if letter_list[j] == val:
                letter_list[j] = idx

    # 숫자를 오름차순으로 정렬(버블 정렬 사용)
    for i in range(n):
        for j in range(n-1,i,-1):
            # 앞의 수가 더 큰 경우 순서 맞바꾸기
            if letter_list[i] > letter_list[j]:
                letter_list[i], letter_list[j] = letter_list[j], letter_list[i]

    # 정렬된 숫자를 이에 대응하는 문자로 전환
    for j in range(n):
        for i in range(10):
            if letter_list[j] == i:
                letter_list[j] = words[i]

    print(f'#{tc}')
    print(*letter_list)