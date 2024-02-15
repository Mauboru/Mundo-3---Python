import moeda

numero = int(input('Digite o preço R$ '))
print(f'O aumento de {moeda.moeda(numero)} é {moeda.moeda(moeda.aumentar(numero))}')
print(f'A diminuição de {moeda.moeda(numero)} é {moeda.moeda(moeda.diminuir(numero))}')
print(f'A metade de {moeda.moeda(numero)} é {moeda.moeda(moeda.metade(numero))}')
print(f'O dobro de {moeda.moeda(numero)} é {moeda.moeda(moeda.dobro(numero))}')