# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros. 
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, 
# imprima uma mensagem de erro. 
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

lista_numeros = input("Digite uma lista de números separados por vírgula: ").split(",")

try:
    lista_inteiros = [int(num) for num in lista_numeros]
    print("Lista de números inteiros:", lista_inteiros)
except ValueError:
    print("Erro: Digite apenas números inteiros.")
