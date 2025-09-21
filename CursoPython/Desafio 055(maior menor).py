maxi = 0
mini = 0

for c in range(1, 6):
    peso = float(input(f"Peso da {c}° pessoa: Kg"))
    if c == 1:
        maxi = peso
        mini = peso
    else:
        if peso > maxi:
            maxi = peso
        if peso < mini:
            mini = peso
print(f"O maior peso foi {maxi}Kg!")
print(f"E o menor peso foi {mini}Kg!")