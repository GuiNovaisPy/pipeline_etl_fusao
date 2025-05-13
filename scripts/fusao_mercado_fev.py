from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv = 'data_raw/dados_empresaB.csv'


#EXTRACT
dados_empresa_a = Dados(path_json)
print(f'nome colunas empresa A: {dados_empresa_a.nomes_colunas}')
print(f'qtd de linhas base empresa A: {dados_empresa_a.qtd_linha}')

dados_empresa_b = Dados(path_csv)
print(f'nome colunas empresa B antes da transformacao: \n {dados_empresa_b.nomes_colunas}')
print(f'qtd de linhas base empresa B: {dados_empresa_b.qtd_linha}')


#TRANSFORM
key_mapping = {
    'Nome do Item':'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)':'Preço do Produto (R$)',
    'Quantidade em Estoque' : 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}
dados_empresa_b.rename_colums(key_mapping)
print(f'nome colunas empresa B apos transformacao: \n {dados_empresa_b.nomes_colunas}')

dados_fusao = Dados.join(dados_empresa_a,dados_empresa_b)
print(f'nome colunas fusao: {dados_fusao.nomes_colunas}')
print(f'qtd de linhas base fusao: {dados_fusao.qtd_linha}')

#LOAD
path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)