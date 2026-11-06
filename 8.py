
limite = int(input("Digite o limite (maior que 1): "))

while limite <= 1:
    limite = int(input("Digite novamente: "))

i = 2
quantidade = 0

while i <= limite:
    soma = 0
    divisor = 1

    while divisor <= i // 2:
        if i % divisor == 0:
            soma += divisor
        divisor += 1

    if soma == i:
        print(f'{i} é perfeito')
        quantidade += 1

    i += 1

if quantidade > 0:
    print(f'Quantidade de números perfeitos encontrados: {quantidade}')
else:
    print("Nenhum número perfeito encontrado")