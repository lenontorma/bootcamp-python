from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

class GeradorDadosEcommerce:
    def __init__(self, seed=42):
        """Inicializa o gerador com seed para reprodução"""
        self.fake = Faker('pt_BR')
        self.fake.seed_instance(seed)
        random.seed(seed)
        
    def gerar_clientes(self, n=500):
        """Gera DataFrame de clientes com: 
        ID, nome, email, localização, data_nascimento e data_cadastro"""
        clientes = []
        for _ in range(n):
            clientes.append({
                'id_cliente': self.fake.unique.uuid4(),
                'nome': self.fake.name(),
                'email': self.fake.unique.email(),
                'cidade': self.fake.city(),
                'estado': self.fake.state_abbr(),
                'data_nascimento': self.fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d'),
                'data_cadastro': self.fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')
            })
        return pd.DataFrame(clientes)
    
    def gerar_produtos(self, n=50):
        """Gera DataFrame de produtos com: 
        ID, nome, categoria, preço, custo e estoque"""
        categorias = ['Eletrônicos', 'Moda', 'Casa', 'Beleza', 'Esportes', 'Alimentos']
        produtos = []
        for _ in range(n):
            custo = round(random.uniform(15, 300), 2)
            margem = random.uniform(0.3, 1.2)  # Margem de 30% a 120%
            produtos.append({
                'id_produto': self.fake.unique.uuid4(),
                'nome': f"Produto {self.fake.unique.word().capitalize()}",
                'categoria': random.choice(categorias),
                'custo': custo,
                'preco': round(custo * (1 + margem), 2),
                'estoque': random.randint(10, 500)
            })
        return pd.DataFrame(produtos)
    
    def gerar_transacoes(self, df_clientes, df_produtos, n=5000):
        """Gera DataFrame de transações vinculando clientes e produtos"""
        transacoes = []
        clientes_ids = df_clientes['id_cliente'].tolist()
        produtos_info = df_produtos.set_index('id_produto').to_dict('index')
        
        for _ in range(n):
            id_cliente = random.choice(clientes_ids)
            id_produto = random.choice(list(produtos_info.keys()))
            preco = produtos_info[id_produto]['preco']
            qtde = random.randint(1, 3)
            
            transacoes.append({
                'id_transacao': self.fake.unique.uuid4(),
                'id_cliente': id_cliente,
                'id_produto': id_produto,
                'data': self.fake.date_time_between(
                    start_date='-1y', 
                    end_date='now'
                ).strftime('%Y-%m-%d %H:%M:%S'),
                'quantidade': qtde,
                'valor_total': round(preco * qtde, 2),
                'canal_venda': random.choice(['Site', 'App', 'Loja Física']),
                'status': random.choices(
                    ['Concluído', 'Devolvido', 'Cancelado'], 
                    weights=[0.9, 0.07, 0.03]
                )[0]
            })
        return pd.DataFrame(transacoes)

# --- Exemplo de uso ---
if __name__ == "__main__":
    print("🛠️ Gerando base de dados de e-commerce...")
    
    gerador = GeradorDadosEcommerce(seed=123)
    
    # Gerar os datasets
    df_clientes = gerador.gerar_clientes(300)
    df_produtos = gerador.gerar_produtos(40)
    df_transacoes = gerador.gerar_transacoes(df_clientes, df_produtos, 2000)
    
    # Salvar em CSV
    df_clientes.to_csv('data/clientes.csv', index=False)
    df_produtos.to_csv('data/produtos.csv', index=False)
    df_transacoes.to_csv('data/transacoes.csv', index=False)
    
    print("✅ Base gerada com sucesso!")
    print(f"📊 Clientes: {len(df_clientes)} registros")
    print(f"📦 Produtos: {len(df_produtos)} registros")
    print(f"💳 Transações: {len(df_transacoes)} registros")