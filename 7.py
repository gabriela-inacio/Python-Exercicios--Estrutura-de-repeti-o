#Questão 7. Sequência de Fibonacci
#A sequência de Fibonacci começa com 0 e 1, e cada número seguinte é a soma dos dois anteriores: 0, 1, 1,
#2, 3, 5, 8, 13, 21, 34, ...
#Escreva um programa em Python que solicite ao usuário um número inteiro positivo n (maior que 0) e exiba
#os n primeiros termos da sequência de Fibonacci. Ao final, o programa deve exibir também a soma de todos
#os termos exibidos.

#Exemplo:
#Quantos termos deseja exibir? 8
#Sequência de Fibonacci: 0 1 1 2 3 5 8 13
#Soma dos termos: 33

#Quantos termos deseja exibir? 1
#Sequência de Fibonacci: 0
#Soma dos termos: 0

num = int(input("Quantos termos deseja : "))

fibo1 = 0 # primeiro numero de fibonacci
fibo2 = 1  # segundo numero de fibonacci

fibo_proximo = 0
soma = 0

i = 0

if num <= 0:
        print("Erro! Digite um número positivo diferente de zero.")
        exit()

while i < num:
        print(fibo1)
        soma = soma + fibo1
        
        fibo_proximo = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = fibo_proximo
       
        i = i + 1

print(f'A soma de {num} termos da Sequência de Fibonacci é {soma}.')