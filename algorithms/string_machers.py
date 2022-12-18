def bruteForce(text, match):
    if len(match) > len(text):
        return False
    for k in range(len(text)):
        j = 0
        while text[k+j] == match[j]:
            j +=1 
            if j == len(match):
                return k
    return False


