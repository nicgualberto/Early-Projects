altura_parede = float(input("Qual a altura da  parede(em metros)? "))
largura_parede = float(input("Qual a largura da parede(em metros)? "))

area = altura_parede * largura_parede
tinta = area // 2

print(f"A quantidade necessária de litros para pintar essa parede é de : {tinta} litros ")
