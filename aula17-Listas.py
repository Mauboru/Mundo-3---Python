# DESAFIO 078 - Maior e Menor valores na lista

# numeros = list()
# maior = 0
# menor = 1000
# posMenor = 0
# posMaior = 0

# for i in range(5):
#     numeros.append(int(input(f"Digite um numero inteiro [{i}]: ")))
#     if numeros[i] > maior:
#         maior = numeros[i]
#         posMaior = i
#     if numeros[i] < menor:
#         menor = numeros[i]
#         posMenor = i

# print(numeros)
# print(f"O maior número da lista é {maior} na posiçao {posMaior}")
# print(f"O menor número da lista é {menor} na posiçao {posMenor}")

# DESAFIO 079 - Valores unicos em uma lista

# numeros = list()
# aux = 0
# opcao = ''

# while opcao in "Ss":
#     aux = int(input('Digite um numero inteiro: '))
#     if aux in numeros:
#         print('Não irei adicionar esse numero repetido!')
#     else:
#         numeros.append(aux)
#         print(numeros)
#     opcao = input('Quer continuar?(s/n)')

# numeros.sort()
# print(numeros)

# DESAFIO 080 - Lista ordenada sem repetições

# numeros = list()

# for i in range(5):
#     aux = int(input(f"Digite um valor: "))
    
#     if len(numeros) == 0:
#         numeros.append(aux)
#         print('Adicionado ao final da lista...')
#     else:
#         adicionado = False
#         for j in range(len(numeros)):
#             if aux <= numeros[j]:
#                 numeros.insert(j, aux)
#                 print(f'Adicionado na posição {j} da lista...')
#                 adicionado = True
#                 break
#         if not adicionado:
#             numeros.append(aux)
#             print('Adicionado ao final da lista...')

# print(numeros)

# DESAFIO 081 - Extraindo dados de uma Lista

# numeros = list()
# digitados = 0

# while True:
#     aux = int(input('Digite um valor: '))
#     numeros.append(aux)
#     continuar = str(input('Quer continuar?(s/n) '))
#     digitados = digitados + 1

#     if continuar in 'Nn':
#         break
# # A) Quantos numeros foram digitados
# print(f'\nForam digitados {digitados} numeros')

# # B) A lista de valores, ordenada de forma decrescente
# numeros.sort(reverse=True)
# print(f'\nDecrescente: {numeros}')

# # C) Se o valor 5 foi digitado e esta ou nao na lista
# if 5 in numeros:
#     print('\nO valor 5 foi digitado na lista')
# else:
#     print('\nO valor 5 não foi digitado na lista')

# DESAFIO 082 - Dividindo valores em várias listas

# numeros = list()
# impares = list()
# pares = list()

# while True:
#     aux = int(input('Digite um valor: '))
#     numeros.append(aux)

#     if aux % 2 == 0:
#         pares.append(aux)
#     else:
#         impares.append(aux)

#     continuar = str(input('Quer continuar?(s/n) '))
#     if continuar in 'Nn':
#         break

# print(f'A lista completa é {numeros}')
# print(f'A lista de pares é {pares}')
# print(f'A lista de impares é {impares}')

# DESAFIO 083 - Validando expressões matemáticas

# expressao = str(input('Digite a expressão: '))
# length = 0

# for i in expressao:
#     length = length + 1
    
#     if i not in '(' and length >= len(expressao):
#         print('Sua expressão é inválida!')
#         break
#     else:
#         if expressao.count('(') == expressao.count(')'):
#             print('Sua expressão é válida!')
#             break