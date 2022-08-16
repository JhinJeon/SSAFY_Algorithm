# 1216. 회문 2

# 박승재님 코드(실행시간 단축)
import sys
sys.stdin = open('input.txt')

#  실행시간을 줄이는 두번째 정답
def circular(string_list):
		#  회문의 길이가 제일 큰 것을 확인하면 되니 M을 역순으로 진행함
    for M in range(100, 0, -1):
        for i in range(100):
            for j in range(100-M+1):
                find = True
                find_row = True
                find_col = True
                for checking in range(M//2):
				#  문자열 처음이랑 끝을 비교 후 틀리면 False를 넣어서 비교하지 않음
                    if find_row and string_list[i][j+checking] != string_list[i][j+M-1-checking]:
                        find_row = False
                    if find_col and string_list[j+checking][i] != string_list[j+M-1-checking][i]:
                        find_col = False
										#  행과 열 둘 다 False 일 때는 최종 find를 False로 주고 반복문 종료
                    if not find_row and not find_col:
                        find = False
                        break
                if find:
                    return M

for test_case in range(10):
    print(f'#{input()}', end=' ')

    string_list = [list(input()) for _ in range(100)]

    print(circular(string_list))

