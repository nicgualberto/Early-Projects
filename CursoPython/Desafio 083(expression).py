expr = str(input('Type a expression: '))
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append('(')
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Your expression is valid!')
else:
    print('Your expression is invalid!')
        
        