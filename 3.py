#Escreva um programa em Python que solicite ao usuário um número inteiro positivo n (maior que 0). O
#programa deve fazer uma contagem regressiva de n até 1 e, para cada número, informar se ele é par ou
#ímpar. Ao final da contagem, exibir "Fim!" e a quantidade total de números pares e ímpares da contagem.

impar = 0
par = 0
i = 0

n = int(input("Digite um número positivo(maior que 0): "))

while n > i:
   
    if n % 2 == 0:
        print(f'{n} é par')
        par = par + 1
    if n % 2 == 1:
        print(f'{n} é impar')
        impar = impar + 1
    n = n - 1

print("Fim!")
print(f'A quantidade de numeros pares é: {par} e de impares é de: {impar}')
