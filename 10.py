# Quantidade de numeros pares em um intervalo

num = int(input("Digite um limite(maior que 4): "))

while num <= 4:
    print("Valor inválido!")
    num = int(input("Digite um limite(maior que 4): "))

i = 3
contador = 0

while i <= num - 2:

    dividir = 2
    primo1 = 1

    while dividir <= i / 2:
        if i % dividir == 0:
            primo1 = 0
        dividir = dividir + 1

   
    dividir = 2
    primo2 = 1

    while dividir <= (i + 2) / 2:
        if (i + 2) % dividir == 0:
            primo2 = 0
        dividir = dividir + 1

    
    if primo1 == 1 and primo2 == 1:
        print(f"({i}, {i + 2})")
        contador = contador + 1

    i = i + 1

print(f"A quantidade de pares encontrados é de:{contador}")