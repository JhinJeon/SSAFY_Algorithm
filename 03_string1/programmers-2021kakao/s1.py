# 숫자 문자열과 영단어

# 문자를 숫자로 바꿔주는 solution 함수 정의
# s = 숫자로 바꿀 문자열
def solution(s):
    # numbers = 문자 자료형으로 된 숫자 리스트
    # numbers를 문자형으로 정의한 이유는 replace 메서드를 사용하기 위함(replace()는 정수를 넣을 수 없음)
    # words = 숫자에 대응되는 단어들 리스트
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    # 문자열 s에서 words에 해당하는 단어를 발견하면 해당 단어를 숫자로 변경
    for i in range(len(words)):
        s = s.replace(words[i], numbers[i])

    # 변경 결과를 정수 형태로 반환
    return int(s)