frase = str(input('Digite uma frase: ')).strip().lower()

inverso = ''

for letra in range(len(frase)-1,-1,-1):
    inverso = inverso+frase[letra]

print(f'\n\033[1m{inverso}\033[m')
