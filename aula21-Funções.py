# DESAFIO 101 - Funções para votação

# from datetime import date

# def voto(idade):
#     if idade >= 16 and idade <= 18 or idade >= 70:
#         msg = 'VOTO OPCIONAL!'
#     elif idade < 16:
#         msg = 'NÃO VOTA!'
#     else:
#         msg = 'VOTO OBRIGATORIO!'
#     return msg

# ano = int(input('Em que ano você nasceu? '))
# idade = date.today().year - ano
# print(f'Com {idade} anos: {voto(idade)}')

# DESAFIO 102 - Função para Fatorial

# def fatorial(n, show=False):
#     f = 1
#     for c in range(n, 0, -1):
#         if show:
#             print(c, end='')
#             if c > 1:
#                 print(' x ', end='')
#             else:
#                 print(f' = ', end='')
#         f *= c
#     return f

# print(fatorial(5, True))        

# DESAFIO 103 - Ficha do Jogador

# def ficha(nome='<desconhecido>', gols=0):
#     print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

# jogador = str(input('Nome do Jogador: '))
# gol = str(input('Número de Gols: '))

# if gol.isnumeric():
#     gol = int(gol)
# else:
#     gol = 0

# if jogador.strip() == '':
#     ficha(gols=gol)
# else:
#     ficha(jogador, gol)

# DESAFIO 104 - Validando entrada de dados em Python

# def leiaInt(msg):
#     ok = False
#     valor = 0

#     while True:
#         n = str(input(msg))
#         if n.isnumeric():
#             valor = int(n)
#             ok = True
#         else:
#             print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
#         if ok:
#             break
#     return valor

# n = leiaInt("Digite um numero: ")
# print(f'Você acabou de digitar o número {n}')

# DESAFIO 105 - Analisando e gerando Dicionários

# def notas(*n, sit=False):
#     nota = list(n)
#     resposta = dict()
    
#     #Pegando qtd de nota
#     resposta['total'] = len(nota)
    
#     #Pegando maior nota
#     maior = 0
#     for i in nota:
#         if i > maior:
#             maior = i
#     resposta['maior'] = maior
    
#     #Pegando menor nota
#     menor = float('inf')
#     for i in nota:
#         if i < menor:
#             menor = i
#     resposta['menor'] = menor
    
#     #Pegando a media das notas
#     resposta['media'] = sum(nota) / len(nota)
    
#     #Pegando a situação
#     if sit:
#         if resposta['media'] > 6:
#             resposta['situação'] = 'BOA!'
#         else:
#             resposta['situação'] = 'RUIM!'
    
#     return resposta

# resposta = notas(5.5, 2.5, 1.5, 9, sit=True)
# print(resposta)

# DESAFIO 106 - Interactive helping system in Python

from time import sleep

c = ('\033[m', # sem cor
     '\033[0;30;41m', # vermelho
     '\033[0;30;42m', # verde
     '\033[0;30;43m', # amarelo
     '\033[0;30;44m', # azul
     '\033[0;30;45m', # roxo
     '\033[7;30m' # branco
     );

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 4)
    sleep(3)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')
    
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    print(c[0], end='')

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    pesquisa = str(input('Função ou Biblioteca > '))
    
    if pesquisa.upper() != 'FIM':    
        ajuda(pesquisa)
    else:
        titulo('ATÉ LOGO!', 1)
        break