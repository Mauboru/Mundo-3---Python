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

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

jogador = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)