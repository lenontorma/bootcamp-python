# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. 
# Use try-except para lidar com divisões por zero e entradas não numéricas. 
# elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try: 
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = str(input("Digite o operador (+, -, *, /): "))

    if operador == "+":
        resultado = num1 + num2
        print(resultado)
    elif operador == "-":
        resultado = num1 - num2 
        print(resultado)
    elif operador == "*":
        resultado = num1 * num2
        print(resultado)
    elif operador == "/":
        if num2 == 0:
            print("Erro: Divisão por zero")
        else:
            resultado = num1 / num2
            print(resultado)
    else:
        print("Operador inválido")
except ValueError:
    print("Digite apenas números")