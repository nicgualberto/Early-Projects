
while True:
    frase = str(input("Digite aqui uma frase (Ou digite 'sair' para encerrar): ")).lower()
    if frase == 'sair':
            print("Muito obrigado por testar o programa! Até mais.")
            break
    dividida = frase.split()
    print(dividida)
    palavra = []
    for p in dividida:
        if p not in palavra:
            vezes = dividida.count(p)
            print(f"Palavra: '{p}' > {vezes} vezes")
            palavra.append(p)