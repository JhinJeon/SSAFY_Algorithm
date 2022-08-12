# 숫자 문자열과 영단어

# 문자를 숫자로 바꿔주는 solution 함수 정의
# s = 숫자로 바꿀 문자열
def solution(s):
    # words = 숫자에 대응되는 단어들 리스트
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # 문자열 s에서 words에 해당하는 단어를 발견하면 그 단어가 뜻하는 숫자로 변경
    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    # 변경 결과를 정수 형태로 반환
    return int(s)