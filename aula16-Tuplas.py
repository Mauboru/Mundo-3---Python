# # DESAFIO 072 - CONTAGEM DE 0 ATE 20 POR EXTENSO
# extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
#            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# numero = 20

# while numero >= 0 and numero <= 20:
#     numero = int(input('Digite um número entre 0 e 20: '))
#     print('O número {} por extenso é {}'.format(numero, extenso[numero]))
# print('FIM')

# #DESAFIO 073 - TABELA CAMPEONATO BRASILEIRO

# times = (
#     "Flamengo", "Corinthians", "Palmeiras", "Grêmio", "Internacional", "Atlético-MG", "Fluminense", "São Paulo", "Cruzeiro", 
#     "Santos", "Botafogo", "Vasco da Gama", "Athletico-PR", "Bahia", "Ceará", "Fortaleza", "Goiás", "Sport", "Atlético-GO", "Coritiba")

# # A) Apenas os 5 primeiro colocados
# print('Apenas os 5 primeiro colocados: ')
# print(times[:5])
# print('-----------------')

# # B) Apenas os 4 ultimos colocados
# print('Apenas os 4 ultimos colocados: ')
# print(times[-4:])
# print('-----------------')

# # C) Uma lista com os times em ordem alfabética
# print('Uma lista com os times em ordem alfabética: ')
# print(sorted(times))
# print('-----------------')

# # D) Em que posição na tabela está o time da chapecoense
# print('Em que posição na tabela está o time do Ceara: ')
# for i in range(0, len(times)):
#     if times[i] == 'Ceará':
#         print('O time do {} está na 14º posição!'.format(times[i], i))
# print('-----------------')

#DESAFIO 074 - GERADOR DE NUMEROS ALEATORIOS (maior e menor)

# import random as rand

# tupla = []
# menor = 10000
# maior = -10000

# for i in range(5):
#     numeros = rand.randint(0, 10)
#     tupla.append(numeros)

#     if numeros < menor:
#         menor = numeros
#     if numeros > maior:
#         maior = numeros

# print("TUPLA GERADA: {}".format(tupla))
# print("O menor número da tupla foi {}".format(menor))
# print("O maior número da tupla foi {}".format(maior))

#DESAFIO 075 - ANALISE DE DADOS 

# tupla = []
# pares = []
# posicao = 0
# nove = 0

# for i in range(4):
#     tupla.append(int(input("Insira um numero inteiro: ")))

# # A) Quantas vezes apareceu o valor 9
# for i in range(4):
#     if tupla[i] == 9:
#         nove = nove + 1
# print("O número 9 apareceu {} vezes".format(nove))

# # B) Em que posição foi digitado o primeiro valor 3
# for i in range(4):
#     if tupla[i] == 3:
#         posicao = i+1
#         break
# print("O numero 3 apareceu primeiro na posição {}".format(posicao))

# # C) Quais foram os números pares
# for i in range(4):
#     if tupla[i] % 2 == 0:
#         pares.append(tupla[i])
# print("Os números pares foram: {}".format(pares))

# DESAFIO 076 - LISTA DE PREÇOS

# tupla = ['Banana', 5.50, 'Maça', 2.25, 'Laranja', 8.75, 'Abacaxi', 2.90]

# print(35*'-')
# print('         LISTAGEM DE PREÇOS')
# print(35*'-')
# print(tupla[0], 20*'.', 'R$ ', tupla[1])
# print(tupla[2], 22*'.', 'R$', tupla[3])
# print(tupla[4], 19*'.', 'R$', tupla[5])
# print(tupla[6], 19*'.', 'R$ ', tupla[7])
# print(35*'-')

# DESAFIO 077 - CONTANDO VOGAIS

palavras = ['josue', 'vitor', 'jarro', 'bola']
letras = []
vogais = {'a', 'e', 'i', 'o', 'u'}

for i in palavras:
    print(f"\nNa palavra {i.upper()} temos ", end='')
    for letra in i:
        if letra.lower() in vogais:
            print(letra, end='')
