#Cores no terminal
print("\033[4;33;45mHello,World!\033[m")
print("\033[7;40mNícolas, você é top!\033[m")

a = 3
b = 1
print(f"Os valores são \033[32m{a}\033[m e \033[34m{b}\033[m!")
    
nome = str(input("Digite aqui seu username: "))
cores = {"limpa": "\033[m",
        "azul" : "\033[34m",
         "roxo" : "\033[35m",
        "amarelo" : "\033[33m",
        "pretoebranco" : "\033[7;30m"}
print("Olá, {}{}{}. Prazer em conhce-lo!!".format(cores["roxo"], nome, cores["limpa"]))