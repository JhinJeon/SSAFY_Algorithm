# 다양한 문장 부호를 기준으로 텍스트 크롤링하기

sample_sentence = '안녕하세요! 만나서 반갑습니다. 누구, 저요?'

impure_text = ['!', '?', ',', '.']

for i in impure_text:
    sample_sentence = sample_sentence.replace(i, '.')

refined_sentence = sample_sentence.split('.')

print(refined_sentence)