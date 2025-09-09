ano = int(input("Digite aqui um ano: "))
if ano % 4 == 0:
    print(f"O ano {ano} é considerado ano BISSEXTO!")
elif ano % 400 == 0:
    print(f"O ano {ano} é considerado ano BISSEXTO!")
else:
    print(f"O ano {ano} não é considerado ano BISSEXTO!")
print("==FIM==")