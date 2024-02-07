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

def fatorial(n, show=True):
    if n == 0 or n == 1:
        return 1
    else:
        if show:
            print(f'{n} x', end=' ')
        return n * fatorial(n-1)
    

print(fatorial(5, show=False))