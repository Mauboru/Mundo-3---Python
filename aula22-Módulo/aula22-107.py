import moeda

numero = int(input('Digite o preço R$ '))
print(f'O aumento de {numero} é {moeda.aumentar(numero)}')
print(f'A diminuição de {numero} é {moeda.diminuir(numero)}')
print(f'A metade de {numero} é {moeda.metade(numero)}')
print(f'O dobro de {numero} é {moeda.dobro(numero)}')