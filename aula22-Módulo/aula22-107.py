from moeda import moedas
import moeda

numero = int(input('Digite o preço R$ '))

print(f'O aumento de {moedas(numero)} é {moeda.aumentar(numero, True)}')
print(f'A diminuição de {moedas(numero)} é {moeda.diminuir(numero)}')
print(f'A metade de {moedas(numero)} é {moeda.metade(numero, True)}')
print(f'O dobro de {moedas(numero)} é {moeda.dobro(numero)}')