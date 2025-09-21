nome = str(input("Digite seu nome completo: ")) #22 carecteres o nome tem
nome_maiusculo = nome.upper()
print(nome_maiusculo)
nome_minusculo = nome.lower()
print(nome_minusculo)
nome_sem_espaço = nome.replace(" ", "")
numero_letra = len(nome_sem_espaço)
print(f"{numero_letra}")
nome_primeiro = nome.split()[0]
nome = len(nome_primeiro)
print(f"{nome}")