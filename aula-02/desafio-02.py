# 1) Solicita ao usuário que digite seu nome
nome_usuario = input('Qual é o seu nome? ')

if nome_usuario.isdigit() or nome_usuario.isspace():
    print('Digite o seu nome, com letras')
    exit()
else:
    pass

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_usuario = float(input('Digite o seu salário: '))
    if salario_usuario < 0:
        print('Erro: O salário não pode ser negativo.')
        exit()
except ValueError as ve:
    print("Digite apenas numeros")
    exit()

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_salario = float(input('Digite o seu bonus salarial: '))
    if bonus_salario < 0:
        print('Erro: O bônus salarial não pode ser negativo.')
        exit()
except ValueError as ve:
    print("Digite apenas numeros")
    exit()

# 4) Calcule o valor do bônus final
calculo_kpi = 1000 + salario_usuario * bonus_salario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f'Olá, {nome_usuario}. O seu bônus foi de {calculo_kpi}, referente ao seu salário de {salario_usuario}')