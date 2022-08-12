# 크로아티아 알파벳
import sys
sys.stdin = open('input.txt')
# 크로아티아 알파벳 리스트
croatian = ['dz=','c=','c-','d-','lj','nj','s=','z=']

# 입력받을 단어
word = input()

# 단어 안에 크로아티아 알파벳이 있으면 문자열 0으로 치환
# 알파벳 개수의 길이를 계산하기 위해 단일 문자로 치환
for c in croatian:
    word = word.replace(c,'0')

# 알파벳 개수(문자열 길이) 출력
print(len(word))