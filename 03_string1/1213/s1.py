# SWEA - string

for k in range(1,11):
    # tc = 테스트 케이스 번호
    # finder = 찾을 문자열
    # string_chrs = 찾을 문자열이 속한 문자열
    # word_count = 문자열을 찾은 개수
    tc = int(input())
    finder = input()
    string_chrs = input()
    word_count = 0

    # 문자열 안에서 인덱스 범위 탐색 결과 finder와 일치하는 경우 word_count += 1
    for i in range(len(string_chrs)-len(finder)+1):
        if string_chrs[i:i+len(finder)] == finder:
            word_count += 1


    print(f'#{tc} {word_count}')