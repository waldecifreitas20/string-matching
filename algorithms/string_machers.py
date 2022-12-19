def bruteForce(text, match):
    # Evita Index out of range
    if len(match) > len(text):
        print(len(match))
        print(len(text))
        return -1

    for k in range(len(text)):
        j = 0
        while text[k+j] == match[j]:
            j +=1 
            if j == len(match):
                return k
            if k+j == len(text):
                return -1

