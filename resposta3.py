diasEvalores = [
1,
22174.1664,

2,
24537.6698,
	
3,
26139.6134,
	
4,
0.0,
	
5,
0.0,
	
6,
26742.6612,
	
7,
0.0,
	
8,
42889.2258,
	
9,
46251.174,
	
10,
11191.4722,
	
11,
0.0,
	
12,
0.0,
	
13,
3847.4823,
	
14,
373.7838,
	
15,
2659.7563,
	
16,
48924.2448,
	
17,
18419.2614,
	
18,
0.0,
	
19,
0.0,
	
20,
35240.1826,
	
21,
43829.1667,
	
22,
18235.6852,
	
23,
4355.0662,
	
24,
13327.1025,
	
25,
0.0,
	
26,
0.0,
	
27,
25681.8318,

28,
1718.1221,
	
29,
13220.495,
	
30,
8414.61
]
contador = 0
total = 0
diasMedia = 0

for posicao, soma in enumerate(diasEvalores):
    if posicao%2 > 0:
        if soma > 0 :
            total += soma
            contador += 1

media = total/contador
contador = 0

for posicao, valor in enumerate(diasEvalores):
    if posicao%2 > 0:
        contador += 1
        print(f'Dia {contador}, Valor: {valor}')

        if contador == 1:
            if valor != 0:
                maior = valor
                menor = valor

        if valor > media: 
            diasMedia += 1

        elif contador > 1:
            if valor != 0:
                if maior < valor:
                    maior = valor
                if menor > valor:
                    menor = valor
        

print(f'\n\033[1mO menor faturamento foi {menor}')
print(f'O maior faturamento foi {maior}')
print(f'Teve {diasMedia} dias que o faturamento diario foi maior que a média\033[m')
    