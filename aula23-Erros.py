# DESAFIO 113 - Funções aprofundadas em Python

# def leiaInt(msg):
#     while True:
#         try:
#             n = int(input(msg))
#         except (ValueError, TypeError):
#             print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
#             continue
#         else:
#             return n
        
# def leiaFloat(msg):
#     while True:
#         try:
#             n = float(input(msg))
#         except (ValueError, TypeError):
#             print('\033[0;31mERRO! Digite um número real válido.\033[m')
#             continue
#         else:
#             return n

# i = leiaInt("Digite um numero inteiro: ")
# r = leiaFloat("Digite um numero real: ")
# print(f'Você acabou de digitar o número inteiro {i} e o número real foi {r}')

# DESAFIO 114 - Site está acessível?

import requests

def verifica_conexao_internet():
    try:
        response = requests.get("https://github.com/Mauboru")  
        if response.status_code == 200:
            return True
        else:
            return False      
        
    except (requests.ConnectionError, requests.ConnectTimeout):
        return False

if verifica_conexao_internet():
    print("O site Mauboru está com conexão com a Internet.")
else:
    print("Sem conexão com a Internet.")