#carro

km = float(input("Digite aqui quantos quilômetros foram percorridos com o carro : "))
aluguel = int(input("Digite aqui por quantos dias ele foi alugado : "))
preco_aluguel = (60 * aluguel) + (km * 0.15)
print(f"O valor do aluguel do carro é de : R$ {preco_aluguel} ")