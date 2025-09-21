salario = float(input("Digite aqui seu salário: R$ "))

if salario >= 1250:
    aumento10 = salario * 0.10
    aumento = aumento10 + salario
    print(f"Seu salário atual é de: R$ {aumento :.2f}")
else:
    aumento15 = salario * 0.15
    aumento2 = salario + aumento15
    print(f"Seu salário atual é de: R$ {aumento2 :.2f}")
print("--FIM--")