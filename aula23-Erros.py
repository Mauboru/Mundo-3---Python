# DESAFIO 113 - Funções aprofundadas em Python

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return n

i = leiaInt("Digite um numero inteiro: ")
r = leiaFloat("Digite um numero real: ")
print(f'Você acabou de digitar o número inteiro {i} e o número real foi {r}')