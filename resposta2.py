contadorusuario = int(input('Digite um número: '))

numero = 0
numeroanterior = 1
fibonacci = 0

while fibonacci != contadorusuario:
    resultado = numero+numeroanterior
    numeroanterior = fibonacci-numero
    fibonacci = resultado+numeroanterior
    if fibonacci > contadorusuario:
        break
    print(f'{fibonacci}... ', end='')

if fibonacci == contadorusuario:
    print(f'\n\033[1;32mO número {contadorusuario} pertence a sequência de Fibonacci\033[m')
else:
    print(f'\n\033[1;31mO número {contadorusuario} não pertence a sequência de Fibonacci\033[m')
