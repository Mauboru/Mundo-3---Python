# Aumentar a porcentagem em 10%
def aumentar(n, aumento=0, format=False):
    porcentagem = (n * aumento) / 100
    aumento = porcentagem + n
    return aumento if format is False else moedas(aumento)

# Diminuir a porcentagem em 10%
def diminuir(n, diminuir=0, format=False):
    porcentagem = (n * diminuir) / 100
    diminuir = n - porcentagem
    return diminuir if format is False else moedas(diminuir)

# Dobro do valor
def dobro(n, format=False):
    valor = 2 * n
    return valor if format is False else moedas(valor)

# Metade do valor
def metade(n, format=False):
    valor = n / 2
    return valor if format is False else moedas(valor)

# Formata os valores
def moedas(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

# Faz um resumo com todas as infos
def resumo(numero, a, d):
    msg = '--------------------------------\n'
    msg += '        RESUMO DO VALOR        \n'
    msg += '--------------------------------\n'
    msg += f'Preço analisado:        {moedas(numero)}\n'
    msg += f'Dobro do preço:        {dobro(numero, True)}\n'
    msg += f'Metade do preço:       {metade(numero, True)}\n'
    msg += f'{a}% de aumento:        {aumentar(numero, a, True)}\n'
    msg += f'{d}% de redução:        {diminuir(numero, d, True)}\n'
    msg += '--------------------------------'
    return print(msg)