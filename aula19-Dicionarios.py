# DESAFIO 090 - Dicionario em Python

# dados = dict()

# dados['nome'] = str(input('Nome: '))
# dados['media'] = float(input('Media: '))

# if dados['media'] >= 6:
#     dados['situacao'] = 'Aprovado'
# else:
#     dados['situacao'] = 'Reprovado'
    
# for k, v in dados.items():
#     print(f'{k} é igual a {v}')
    
# DESAFIO 091 - Jogo de Dados em Python

# from random import randint
# from time import sleep
# from operator import itemgetter

# jogadores = {
#     'jogador1': randint(0,10),
#     'jogador2': randint(0,10),
#     'jogador3': randint(0,10),
#     'jogador4': randint(0,10)
# }

# ranking = dict()

# print('Valores Sorteados:')
# for k, v in jogadores.items():
#     print(f'O {k} tirou {v}')
#     sleep(1)

# ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
# print('Ranking dos jogadores: ')
# for i, v in enumerate(ranking):
#     print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
#     sleep(1)

# DESAFIO 092 - Cadastro de Trabalhador em Python

# from datetime import date

# dados = dict()

# dados['nome'] = str(input('Nome: '))
# ano = int(input('Ano de Nascimento: '))
# dados['idade'] = date.today().year - ano
# dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

# if dados['ctps'] != 0:
#     dados['contratacao'] = int(input('Ano de Contratação: '))
#     dados['salario'] = float(input('Salário: R$ '))
#     dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - date.today().year)

# print(20*'-=')
# for k, v in dados.items():
#     print(f' - {k} tem o valor {v}')

# DESAFIO 093 - Cadastro de Jogador de Futebol

# dados = dict()
# gols = []
# soma = 0

# dados['nome'] = str(input('Nome do Jogador: '))
# partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

# for i in range(partidas):
#     gols.append(int(input(f'Quantos gols na partida {i}? ')))
#     soma = soma + gols[i]
# dados['gols'] = gols
# dados['total'] = soma

# print(16*'=-')
# print(dados)
# print(16*'=-')

# for k, v in dados.items():
#     print(f'O campo {k} tem o valor {v}')
# print(16*'=-')

# print(f'O {dados["nome"]} jogou {partidas} partidas.')
# for i in range(partidas):
#     print(f'=> Na partida {i}, fez {dados["gols"][i]} gols.')
# print(f'Foi um total de {soma} gols.')

# DESAFIO 094 - Unindo dicionários e listas

# pessoas = list()
# mulheres = list()
# soma_idade = 0

# while True:
#     dados = dict()
#     dados['nome'] = str(input('Nome: '))
#     sexo = str(input('Sexo: [M/F] '))
#     while sexo not in 'mMfF':
#         print('ERRO! Responda apenas M ou F.')
#         sexo = str(input('Sexo: [M/F] '))
#     dados['sexo'] = sexo
#     dados['idade'] = int(input('Idade: '))
#     soma_idade = soma_idade + dados['idade']
    
#     if dados['sexo'] in 'Ff':
#         mulheres.append(dados['nome'])
#     pessoas.append(dados)
    
#     continuar = str(input('Quer continuar (s/n)? '))
#     while continuar not in 'sSnN':
#         print('ERRO! Responda apenas S ou N.')
#         continuar = str(input('Quer continuar (s/n)? '))
    
#     if continuar in 'nN':
#         break

# print(12*'-=')
# print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
# print(f'B) A média de idade é de {soma_idade / len(pessoas):.2f} anos.')
# print(f"C) As mulheres cadastradas foram {', '.join(mulheres)}")
# print('D) Lista de pessoas que estão acima da média:')
# for p in pessoas:
#     if p['idade'] >= soma_idade / len(pessoas):
#         for k, v in p.items():
#             print(f'{k} = {v};', end='')
#         print()
# print('<< ENCERRADO >>')

# DESAFIO 095 - Aprimorando os Dicionários

jogadores = []
codigo = 0

while True:
    dados = dict()
    gols = []
    soma = 0
    dados['codigo'] = codigo
    codigo = codigo + 1
    dados['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))

    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
        soma = soma + gols[i]
    dados['gols'] = gols
    dados['total'] = soma
    
    jogadores.append(dados)
    
    continuar = str(input('Quer continuar (s/n)? '))
    if continuar in 'nN':
        break
    
print(12*"=-")
print('cod   nome    gols   total')
print(12*'--')
for i in jogadores:
    print(f'{i["codigo"]}   {i["nome"]}  {i["gols"]}    {i["total"]}')
        
while True:
    opcao = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opcao == 999:
        break

    if opcao >= len(jogadores):
        print('Código de jogador inválido! Tente novamente.')
        continue

    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opcao]["nome"]}')
    for i, gols in enumerate(jogadores[opcao]['gols']):
        print(f'No jogo {i+1} fez {gols} gols.')