# Aumentar a porcentagem em 10%
def aumentar(n, format=False):
    porcentagem = (n * 10) / 100
    aumento = porcentagem + n
    return aumento if format is False else moedas(aumento)

# Diminuir a porcentagem em 10%
def diminuir(n, format=False):
    porcentagem = (n * 10) / 100
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