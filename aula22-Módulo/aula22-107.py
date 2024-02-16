from utilidadesCeV.moeda import moedas
from utilidadesCeV import moeda
from utilidadesCeV import dado

numero = dado.leiaDinheiro('Digite o preço R$ ')
moeda.resumo(numero, 20, 12)