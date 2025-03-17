##  Exercício 21: Conversor de Temperatura
## Escreva um programa que converta a temperatura de Celsius para Fahrenheit. 
## O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. 
## Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

try:
    graus_celsius = float(input("Digite a temperatura em Celsius: "))
    calculo = (graus_celsius *9/5) + 32
    print(f"A temperatura em Fahrenheit é: {calculo}")
except:
    print("Digite apenas numeros")

