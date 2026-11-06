#Questão 6. Calculadora
#Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
#• adição (opção 1)
#• subtração (opção 2)
#• multiplicação (opção 3)
#• divisão (opção 4)
#• saída (opção 5)

#O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao
#menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5).



while True:
    operacao = input("Informe a operção que deseja realizar: \nAdição(1)\nSubtração(2)\nMultiplicação(3)\nDivisão(4)\nSair(5)= ")

    if operacao == "5":
        print(f'Programa encerrado!')
        break

    num1 = float(input("Informe o primeiro o número: "))
    num2 = float(input("Informe o segundo número: "))

    
    if operacao == "1":
        print(f'O resuldato da adição de {num1} + {num2} é {num1 + num2}')
    
    elif operacao == "2":
        print(f'O resuldato da subtração de {num1} - {num2} é {num1 - num2}')

    elif operacao == "3":
        print(f'O resuldato da multiplição de {num1} x {num2} é {num1 * num2}')
    
    elif operacao == "4":
        if num2 == 0:
            print(f'ERRO! Divisão por zero, escolha outro numero.')
        else:
            print(f'O resuldato da divisão de {num1} / {num2} é {num1 / num2}')

    else:
        print(f'Operação invalida!')

