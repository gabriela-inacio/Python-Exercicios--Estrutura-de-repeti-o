#Numero imvertido, quantidade de digitos e soma dos digitos
num = int(input("Digite um número inteiro positivo: "))

while num <= 0:
    print("Valor inválido!")
    num = int(input("Digite um número inteiro positivo: "))

original = num
invertido = 0
quantidade = 0
soma = 0

while num > 0:
    digito = num % 10
    invertido = invertido * 10 + digito
    soma = soma + digito
    quantidade = quantidade + 1
    num = num // 10

if original == invertido:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")

print(f" O número invertido é: {invertido}, a quantidade de dígitos desse número é: {quantidade}, e a soma dos seus dígitos é: {soma}")