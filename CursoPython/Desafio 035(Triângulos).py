print("ANALISADOR DE TRIÂNGULOS")

reta1 = float(input("Digite aqui o valor da primeira reta: "))
reta2 = float(input("Digite o valor da segunda: "))
reta3 = float(input("Digite o valor da terceira: "))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("É possível formar um triângulo!")
else:
    print("Não é possível formar um triângulo!")