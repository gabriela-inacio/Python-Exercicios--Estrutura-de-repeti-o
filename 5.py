#Faç̧a um programa que some os números ímpares contidos em um intervalo definido pelo usuário. O usuário
# define o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números
###termina.
#Exemplo de tela de saída:
#Digite o valor inicial: 5
#Digite o valor final: 10
#Soma dos ímpares neste intervalo: 21



num1 = int(input("Informe o valor inicial: "))
num2 = int(input("Informe o valor final: "))


if num1 > num2:
        print(f"Intervalo de valores invalido") 
else:
        i = num1
        soma = 0
        
        while i <= num2:
                if i % 2 != 0:
                        soma = soma + i
                i = i + 1
                
print(f"Soma dos ímpares neste intervalo:{soma}")