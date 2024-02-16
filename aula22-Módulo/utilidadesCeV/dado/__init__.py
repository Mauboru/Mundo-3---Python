def leiaDinheiro(p):
    ok = False
    valor = 0

    while True:
        n = str(input(p))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um valor monetário válido.\033[m')
        if ok:
            break
    return valor