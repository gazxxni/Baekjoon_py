import math
def solution(n, words):
    answer = []
    prev = words[0]
    p_words = [prev]
    num = 2
    for word in words[1:]:
        number = num % n if num % n != 0 else n
        if prev[-1] == word[0]:
            if word in p_words:
                return [number, math.ceil(num / n)]
            
            else:
                num += 1
                prev = word
                p_words.append(word)
        else:      
            return [number, math.ceil(num / n)]
        
    return [0, 0]