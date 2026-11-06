#Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste
#número na saída.
#Entrada.: 103
#Saída = 1 + 0 + 3 = 4

soma = 0
num = int(input("Informe um numero:"))

while num > 0:
    digito = num % 10
    soma = soma + digito
    num = num // 10

print(f"A soma dos digitos do numero informado é {soma}.")
    


