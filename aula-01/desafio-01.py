nome_usuario = input('Qual é o seu nome? ')

salario_usuario = float(input('Digite o seu salário: '))

bonus_salario = float(input('Qual é o seu bônus salarial? '))

calculo_kpi = 1000 + salario_usuario * bonus_salario

print(f'Olá, {nome_usuario}. O seu bônus foi de {calculo_kpi}')