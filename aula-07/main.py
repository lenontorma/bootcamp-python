# Ler o arquivo CSV e carregar os dados.
# Processar os dados em um dicionário, onde a chave é a categoria, e o valor é uma lista de dicionários, cada um contendo informações do produto (Produto, Quantidade, Venda).
# Calcular o total de vendas (Quantidade * Venda) por categoria.

import csv

nome_arquivo = 'dados_produtos.csv' 

def ler_arquivo_csv(nome_arquivo):
    dados_por_categoria = {}
    
    with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        
        for linha in leitor:
            categoria = linha['Categoria']
            produto = {
                'Produto': linha['Produto'],
                'Quantidade': int(linha['Quantidade']),
                'Venda': float(linha['Venda'])
            }
            
            if categoria not in dados_por_categoria:
                dados_por_categoria[categoria] = []
            
            dados_por_categoria[categoria].append(produto)
    
    return dados_por_categoria

def calcular_total_vendas_por_categoria(dados):
    totais_por_categoria = {}
    
    for categoria, produtos in dados.items():
        total = sum(prod['Quantidade'] * prod['Venda'] for prod in produtos)
        totais_por_categoria[categoria] = total
    
    return totais_por_categoria


dados_processados = processar_dados_csv(nome_arquivo)
totais_vendas = calcular_total_vendas_por_categoria(dados_processados)

print("Dados processados por categoria:")
for categoria, produtos in dados_processados.items():
    print(f"\nCategoria: {categoria}")
    for produto in produtos:
        print(f"  Produto: {produto['Produto']}, Quantidade: {produto['Quantidade']}, Venda: R${produto['Venda']:.2f}")

print("\nTotal de vendas por categoria:")
for categoria, total in totais_vendas.items():
    print(f"{categoria}: R${total:.2f}")