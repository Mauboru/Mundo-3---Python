# DESAFIO 084 - Lista composta e análise de dados

# pessoas = []
# dados = []
# mais_pesados = []
# menos_pesados = []
# maior_peso = 0
# menor_peso = 1000

# while True:
#     dados.append(str(input('Nome: ')))
#     dados.append(float(input('Peso: ')))
#     pessoas.append(dados[:])
#     dados.clear()
    
#     continuar = str(input('Quer cotinuar (s/n)? '))
#     if continuar in 'nN':
#         break

# #Identifica maior e menor peso
# for p in pessoas:
#     if p[1] > maior_peso:
#         maior_peso = p[1]
#     if p[1] < menor_peso:
#         menor_peso = p[1]
        
# #Identifica quem foram os mais pesados e mais leves
# for p in pessoas:
#     if maior_peso == p[1]:
#         mais_pesados.append(p[0])
#     if menor_peso == p[1]:
#         menos_pesados.append(p[0])

# print(f'Ao todo você cadastrou {len(pessoas)} pessoas')
# print(f'O maior peso foi de {maior_peso} Kg. Peso de {mais_pesados}')
# print(f'O menor peso foi de {menor_peso} Kg. Peso de {menos_pesados}')

# DESAFIO 085 - Lista com pares e impares

# numeros = []
# pares = []
# impares = []

# for i in range(1, 8):
#     entrada = int(input(f'Digite o {i}o. valor: '))
    
#     if entrada % 2 == 0:
#         pares.append(entrada)
#     else:
#         impares.append(entrada)

# numeros.append(pares)
# numeros.append(impares)

# print(20 * '-=')
# print(numeros)
# print(f'Os valores pares digitados foram: {numeros[0]}')
# print(f'Os valores impares digitados foram: {numeros[1]}')

# DESAFIO 086 - Matriz em Python

# matriz = []

# for i in range(3):
#     linha = []
#     for j in range(3):
#         entrada = int(input(f'Digite um valor para [{i}, {j}]: '))
#         linha.append(entrada)
#     matriz.append(linha)

# print(20 * '-=')

# for i in range(3):
#     for j in range(3):
#         print(f'[{matriz[i][j]:^5}]', end='')
#     print()

# DESAFIO 087 - Mais sobre Matriz em Python

# matriz = []
# pares = 0
# terceira_coluna = 0
# maior_segunda = 0

# for i in range(3):
#     linha = []
#     for j in range(3):
#         entrada = int(input(f'Digite um valor para [{i}, {j}]: '))
#         if entrada % 2 == 0:
#             pares = pares + entrada
#         if j == 2:
#             terceira_coluna = terceira_coluna + entrada
#         linha.append(entrada)
#     if i == 1:
#             if entrada > maior_segunda:
#                 maior_segunda = entrada
#     matriz.append(linha)

# print(20 * '-=')

# for i in range(3):
#     for j in range(3):
#         print(f'[{matriz[i][j]:^5}]', end='')
#     print()
    
# print(20 * '-=')
# print(f'A soma dos valores pares é {pares}')
# print(f'A soma dos valores da terceira coluna é {terceira_coluna}')
# print(f'O maior valor da segunda linha é {maior_segunda}')

# DESAFIO 088 - Palpites para a Mega Sena

# from time import sleep
# from random import randint

# def numero_repetido(sorteado):
#     numero = randint(1, 100)
#     while numero in sorteado:
#         numero = randint(1, 100)
#     return numero

# sorteado = []

# print(12*'--')
# print('   JOGA NA MEGA SENA')
# print(12*'--')

# sorteios = int(input('Quantos jogos você quer que eu sorteie? '))

# print(f'-=-=-= SORTEANDO {sorteios} JOGOS -=-=-=')

# for i in range(sorteios):
#     for j in range(6):
#         sorteado.append(numero_repetido(sorteado))
#     sleep(.7)
#     sorteado.sort()
#     print(f'Jogo {i+1}: {sorteado}')
#     sorteado.clear()
# print(f'-=-=-= < BOA SORTE! > -=-=-=')

# DESAFIO 089 - Boletim com listas compostas

alunos = []

while True:
    dados = []
    dados.append(len(alunos) + 1)
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    dados.append((dados[2] + dados[3]) / 2)
    alunos.append(dados[:])

    continuar = str(input('Quer continuar (s/n)? '))
    if continuar in 'Nn':
        break

print(20 * '-=')
print('No. NOME               MÉDIA')
print('--------------------------')

for aluno in alunos:
    print(f'{aluno[0]:<4}{aluno[1]:<20}{aluno[4]:.1f}')
    
print('--------------------------')

while aluno != 999:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    
    if 1 <= aluno <= len(alunos):
        print(f'Notas de {alunos[aluno-1][1]} são {alunos[aluno-1][2]}, {alunos[aluno-1][3]}')
    else:
        print('Aluno não encontrado. Tente novamente.')