import pandas as pd
import numpy as np

print("⚙️ PIPELINE DE ENGENHARIA DE DADOS - SIMULAÇÃO CORPORATIVA ISOLADA ⚙️\n")

def gerar_dados_em_massa():
    """Módulo de Infraestrutura: Cria 10.000 linhas de dados de vendas de raiz"""
    np.random.seed(42) # Garante que os números são consistentes
    
    # Criar listas de dados simulados
    clientes = ['Empresa_Alfa', 'Empresa_Beta', 'Empresa_Gama', 'Delta_Sistemas', 'Omega_Logistica']
    regioes = ['Norte', 'Sul', 'Centro', 'Lisboa', 'Porto']
    
    print("⏳ A gerar 10.000 registos de vendas nos bastidores...")
    
    dados = {
        'ID_Venda': range(1000, 11000),
        'Cliente': np.random.choice(clientes, 10000),
        'Regiao': np.random.choice(regioes, 10000),
        'Quantidade': np.random.randint(1, 50, 10000),
        'Preco_Unitario': np.random.uniform(10.50, 500.00, 10000)
    }
    
    return pd.DataFrame(dados)

def processar_pipeline(df_bruto):
    """Módulo de Lógica: Faz o tratamento de dados de nível empresarial"""
    # 1. CÁLCULO DE COLUNA: Criar a coluna de Faturação Total (Qtd * Preço)
    df_bruto['Faturacao_Total'] = df_bruto['Quantidade'] * df_bruto['Preco_Unitario']
    
    # 2. FILTRAGEM DE SEGURANÇA: Isolar apenas vendas acima de 5.000 Euros (Grandes Contas)
    grandes_vendas = df_bruto[df_bruto['Faturacao_Total'] > 5000.00].copy()
    
    # 3. AGRUPAMENTO ESTATÍSTICO: Calcular o total faturado e a quantidade média por Região
    relatorio_regiao = grandes_vendas.groupby('Regiao').agg(
        Total_Faturado=('Faturacao_Total', 'sum'),
        Quantidade_Media=('Quantidade', 'mean')
    ).reset_index()
    
    # 4. ORDENAÇÃO: Ordenar o mercado mais lucrativo para o menos lucrativo
    relatorio_final = relatorio_regiao.sort_values(by='Total_Faturado', ascending=False)
    return relatorio_final

# --- EXECUÇÃO DO FLUXO DO LABORATÓRIO ---
df_vendas = gerar_dados_em_massa()

print("\n--- AMOSTRA DOS DADOS BRUTOS GERADOS (PRIMEIRAS 5 LINHAS) ---")
print(df_vendas.head())
print("------------------------------------------------------------\n")

# Processar as 10.000 linhas através da lógica do Pandas
relatorio_corporativo = processar_pipeline(df_vendas)

print("--- RELATÓRIO EXECUTIVO FINAL (PROCESSADO EM MICROSEGUNDOS) ---")
# Formatamos os números para parecerem dinheiro real (Euros)
relatorio_corporativo['Total_Faturado'] = relatorio_corporativo['Total_Faturado'].map('€{:,.2f}'.format)
relatorio_corporativo['Quantidade_Media'] = relatorio_corporativo['Quantidade_Media'].map('{:.1f} un'.format)
print(relatorio_corporativo.to_string(index=False))
print("----------------------------------------------------------------\n")

# Exportação direta para o disco
relatorio_corporativo.to_csv('auditoria_grandes_contas.csv', index=False)
print("💾 Sucesso! O ficheiro 'auditoria_grandes_contas.csv' foi gravado localmente.")



