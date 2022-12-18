from algorithms import string_machers as machers
from time import time as runtime
texts = {
    '500': '',
    '1000': '',
    '1500': '',
    '2000': '',
    '5000': '',
}

# Carrega textos dinâmicamente
text_lengths = ['500', '1000', '1500', '2000', '5000']
for text_length in text_lengths:
    with open(f'./texts/text{text_length}.txt', mode='r', encoding='utf-8') as text:
        text_body = ''
        for line in text:
            text_body += ''.join(line)
        texts[text_length] = text_body


for text_length in text_lengths:
    with open(f'./results/text{text_length}.txt', mode='w+', encoding='utf-8') as text:
        word = 'modificações'
        text.write(f'==============================================\n')
        text.write('# BUSCA EM 500 PALAVRAS\n')
        text.write(f'==============================================\n')
        average_time = 0
        for iteration in range(10):
            startTime = runtime().real
            index = machers.bruteForce(texts[text_length], word)
            finishTime = runtime().real - startTime
            average_time += finishTime
            text.write(' - FORCA BRUTA\n')
            text.write(f'    ITERAÇÃO: {iteration}\n')
            text.write(f'    PALAVRA: {word}\n')
            text.write(f'    INDÍCE ENCONTRADO: {index}\n')
            text.write(f'    TEMPO DE EXECUÇÃO: {finishTime}\n')
            text.write(f'-------------------------------------------\n')
        
        text.write(f'TEMPO MÉDIO DE EXECUÇÃO: {average_time/10}\n')
        text.write(f'==============================================\n')
