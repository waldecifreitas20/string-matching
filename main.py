from algorithms import string_machers as machers
from time import time as runtime
from random import choice


WORSE_CASE = 'PIOR' 
RANDOM_CASE = 'LEATÓRIO'
BETTER_CASE = 'MELHOR'

text_lengths = ['500', '1000', '1500', '2000', '5000']

# Retorna o conteudo do arquivo de texto
def loadText(path):
    text_body = ''
    with open(path, mode='r', encoding='utf-8') as text:
            for line in text:
                text_body += ''.join(line)
    return text_body

def test(case) :
    global WORSE_CASE, BETTER_CASE, RANDOM_CASE
    texts = {
        '500': '',
        '1000': '',
        '1500': '',
        '2000': '',
        '5000': '',
    }


    # Carrega textos dinâmicamente
    for text_length in text_lengths:
        path = f'./texts/text{text_length}.txt'
        texts[text_length] = loadText(path)


    word = ''
    folder=''
    # A palavra não existe no texto
    if case == WORSE_CASE:
        word = 'lksjdfjdf'
        folder = 'worse'
    
    # A palavra é a primeira no texto
    elif case == BETTER_CASE:
        word=  'Estratégias'
        folder = 'better'
    
    # A palvra pode estar em qualquer parte do texto ou não
    else:
        text = list(texts['5000'].split(' '))
        word=  choice(text)
        folder = 'random'

    
    # Executa os testes
    for text_length in text_lengths:
        with open(f'./results/{folder}/text{text_length}.txt', mode='w+', encoding='utf-8') as text:
            text.write(f'==============================================\n')
            text.write('# BUSCA EM 500 PALAVRAS\n')
            text.write(f'==============================================\n')
            average_time = 0
            iterations = 1000
            for iteration in range(iterations):
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
            
            text.write(f'TEMPO MÉDIO DE EXECUÇÃO: {average_time/iterations}\n')
            text.write(f'==============================================\n')


cases = [RANDOM_CASE, BETTER_CASE, WORSE_CASE]
for case in cases:
    test(case)