croatian = ['dz=','c=','c-','d-','lj','nj','s=','z=']

word = input()
word.strip('=')

for c in croatian:
    replace_word = word.replace(c,'0')
    word = replace_word

print(len(word))