def leiaDinheiro(p):
    ok = False
    valor = 0
    while True:
        p = str(input(p)).replace(',','.').strip()
        if p.isnumeric():
            valor = float(p)
            ok = True
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.!\033[m')
        if ok:
            break
    return valor
