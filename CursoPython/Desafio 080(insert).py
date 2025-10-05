numbers = []

for c in range(0,5):
    n = int(input('Type a value: '))
    if c == 0 or n > numbers[-1]:
        numbers.append(n)
    else:
        pos = 0
        while pos < len(numbers):
            if n  <= numbers[pos]:
                numbers.insert(pos, n)
                break
            pos += 1
print(f'Os valores da lista : {numbers}')