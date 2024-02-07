# DESAFIO 101 - Funções para votação

from datetime import date

def voto(idade):
    if idade >= 16 and idade <= 18 or idade >= 70:
        msg = 'VOTO OPCIONAL!'
    elif idade < 16:
        msg = 'NÃO VOTA!'
    else:
        msg = 'VOTO OBRIGATORIO!'
    return msg

ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
print(f'Com {idade} anos: {voto(idade)}')