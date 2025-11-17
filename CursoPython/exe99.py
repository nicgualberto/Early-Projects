import time


def maior(*num):
    count = maior = 0
    print('-=' * 20)
    print('Analisando valores...')
    time.sleep(1)
    for valor in num:
        print(f'{valor} .', end='')
    print(
        f'Foram analisados {len(num)} números.  O maior valor foi {max(num)}.')


maior(1, 43, 7, 8)
maior(2, 3, 4, 5, 67)
maior(2, 90)
