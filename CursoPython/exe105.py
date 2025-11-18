def notas(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] > + 7:
            print('\033[1;32mEXCELENTE\033[m')
    else:
        print('\033[1;31mRUIM\033[m')

    return r


resp = notas(12, 5, 6, sit=True)
print(resp)
