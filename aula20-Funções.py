# DESAFIO 096 - Função que calcula área

# def calcula_area(largura, comprimento):
#     area = largura * comprimento
#     print(f'A área de um terreno {largura}x{comprimento} é de {area}m².')

# print('Controle de Terrenos')
# print(12*'-')

# largura = float(input('LARGURA (m): '))
# comprimento = float(input('COMPRIMENTO (m): '))

# calcula_area(largura, comprimento)

# DESAFIO 097 - Um print especial

# def print_especial(palavra):
#     tam = len(palavra) + 2
#     print(tam*'~')
#     print(' ' + palavra + ' ')
#     print(tam*'~')
    
# print_especial(str(input('Digite algo: ')))

# DESAFIO 098 - Função de Contador

# from time import sleep

# def contador(inicio, final, passo):
#     print(15*'-=')
#     print(f'Contagem de {inicio} até {final} de {passo} em {passo}')
    
#     while True:
#         sleep(.6)
#         print(inicio)
        
#         #verificando se soma ou subtrai
#         if inicio > final:
#             inicio -= passo
#             if inicio <= final:
#                 break
#         else:
#             inicio += passo
#             if inicio > final:
#                 break
#     sleep(.6)
#     print(final)
#     print('\nFIM!')
    
# # contador(1, 10, 1)

# print('Agora é sua vez de personalizar a contagem!')
# inicio = int(input('Inicio: '))
# final = int(input('Final: '))
# passo = int(input('Passo: '))

# contador(inicio, final, passo)

# DESAFIO 099 - Função que descobre o maior

# def analisa(valores):
#     print(16*'-=')
#     print('Analisando os valores passados...')
#     print(f'{valores} Foram informados {len(valores)} ao todo.')
    
#     maior = valores[0]
    
#     for i in valores:
#         if i > maior:
#             maior = i
    
#     print(f'O maior valor informado foi {maior}')
    
# analisa([5, 2, 3 , 4, 9])

# DESAFIO 100 - Funções para sortear e somar

from random import randint

numeros = list()

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
    print('PRONTO!')
    
def somaPares(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')
 
sorteia(numeros)
somaPares(numeros)