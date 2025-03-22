# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. 
# Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero". 
# Adicionalmente, identifique se o número é "par" ou "ímpar".


try:
    num = float(input("Digite um número:"))
    if num >0:
        print("O número digitado é positivo")
    elif num <0:
        print("O número digitado é negativo")
    else:
        print("O número digitado é zero")
except:
    print("Digite apenas números")

   