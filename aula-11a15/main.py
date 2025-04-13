import pandas as pd
import time


class ProcessadorDados:
    def __init__(self):
        self._carregar_dados()

    def _carregar_dados(self) -> None:
        """Carrega os DataFrames e valida arquivos."""
        try:
            self.transacoes_df = pd.read_csv("data/transacoes.csv")
            self.clientes_df = pd.read_csv("data/clientes.csv")
            self.produtos_df = pd.read_csv("data/produtos.csv")
        except FileNotFoundError as e:
            raise Exception("Erro ao carregar dados: verifique os arquivos CSV.")

    def validar_email(self):
        if 'email' in self.clientes_df.columns:
            self.emails_validos = self.clientes_df['email'].str.contains('@', na=False)
            print("Verificando os emails dos clientes...")
            time.sleep(1)
            if self.emails_validos.all():
                print("Todos os e-mails são válidos.")
            else:
                invalidos = self.clientes_df[~self.emails_validos]
                print(f'Os seguintes e-mails estão invalidos: \n{invalidos}')
        else:
            print("Coluna 'Email' não encontrada no dataframe, nao foi possível realizar a verificação")
            
    
    def verificador_qtd_invalida(self):
        if 'quantidade' in self.transacoes_df.columns:
            qt_invalida = self.transacoes_df[self.transacoes_df['quantidade'] <= 0].index
            sem_valores_invalidos = self.transacoes_df.drop(qt_invalida)
            self.transacoes_tratada = pd.DataFrame(sem_valores_invalidos)
            return self.transacoes_tratada

    def analisador(self):
        vendas_por_produto = self.transacoes_tratada.groupby('id_produto')['quantidade'].sum().reset_index()
        produtos_mais_vendidos = vendas_por_produto.merge(self.produtos_df[['categoria', 'nome', 'id_produto']], on='id_produto', how='left')
        top_5_produtos = produtos_mais_vendidos.sort_values(by = 'quantidade',ascending= False).head(5)
        print(f'Segue o Top 5 produtos mais vendidos: \n{top_5_produtos.to_string(index=False)}')

        cliente_por_gasto = self.transacoes_tratada.groupby('id_cliente')['valor_total'].sum().reset_index()
        clientes_mais_gastam = cliente_por_gasto.merge(self.clientes_df[['nome', 'estado', 'data_nascimento', 'id_cliente']], on='id_cliente', how='left')
        top_10_clientes = clientes_mais_gastam.sort_values(by = 'valor_total',ascending= False).head(10)
        print(f'Segue o nosso top 10 clientes: \n {top_10_clientes.to_string(index=False)}')

       

processar = ProcessadorDados()
processar.validar_email()
processar.verificador_qtd_invalida()  
processar.analisador()
