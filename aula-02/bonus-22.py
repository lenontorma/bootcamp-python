## Exercício 22: Verificador de Palíndromo
## Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
## Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

try:
    frase = input("Digite uma frase: ")
    if isinstance(frase, str):
        frase = frase.lower()
        frase = frase.replace(" ", "")
        frase = frase.replace(".", "")
        frase = frase.replace(",", "")
        frase = frase.replace(";", "")
        frase = frase.replace(":", "")
        frase = frase.replace("!", "")
        frase = frase.replace("?", "")        
        frase_invertida = frase[::-1]
        if frase == frase_invertida:
            print("A frase digitada é um palíndromo")
        else:                
            print("A frase digitada nao é um palíndromo")
    else:
        print("Digite uma frase")
except: 
    print("Digite uma frase")    