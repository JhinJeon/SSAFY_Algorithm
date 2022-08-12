def solution(s):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(words)):
        s_replace = s.replace(words[i],numbers[i])
        s = s_replace
            
    return int(s)