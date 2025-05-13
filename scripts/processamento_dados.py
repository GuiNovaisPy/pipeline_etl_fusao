import json
import csv

class Dados:
    def __init__(self,path):
        self.path = path
        self.dados = self._leitura_dados()
        self.nomes_colunas = self._get_colums()
        self.qtd_linha = self._size_data()
        
    def _leitura_json(self):
        with open(self.path,'r') as file:
            dados_json= json.load(file)
        return dados_json

    def _leitura_csv(self):
        list_dados_csv = []
        with open(self.path,'r') as file:
            spam_reader = csv.DictReader(file,delimiter=',') #objeto leitor
            for row in spam_reader:
                list_dados_csv.append(row)
        return list_dados_csv

    def _leitura_dados(self):
        dados = []
        
        if isinstance(self.path,list):
            dados = self.path  
            self.path = 'lista em memoria'
        elif self.path.endswith('.csv'):
            dados = self._leitura_csv()
        elif self.path.endswith('.json'):
            dados = self._leitura_json()
          
        return dados

    def _get_colums(self):
        inicio = 0
        final = -1
        if len(list(self.dados[inicio].keys())) > len(list(self.dados[final].keys())):
            return list(self.dados[inicio].keys())
        return list(self.dados[final].keys())
    
    def rename_colums(self,key_mapping):
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key,value in old_dict.items():#retorna chave e valor 
                dict_temp[key_mapping[old_key]] = value #alterando o nome da chave com base no mapeamento
            new_dados.append(dict_temp)
        self.dados = new_dados
        self.nomes_colunas = self._get_colums()
        
    def _size_data(self):
        return len(self.dados)
    
    @staticmethod
    def join(dados_a:'Dados',dados_b:'Dados'):
        combined_list = []
        combined_list.extend(dados_a.dados)
        combined_list.extend(dados_b.dados)
        return Dados(combined_list)
    
    def _transformando_dados_tabela(self):
        dados_combinados_tabela = [self.nomes_colunas]
        for row in self.dados:
            linha = []
            for coluna in self.nomes_colunas:
                linha.append(row.get(coluna,'indisponivel')) #preenchendo com default para os que nao possuem
            dados_combinados_tabela.append(linha)
        return dados_combinados_tabela
    
    def salvando_dados(self,path):
        dados_combinados_tabela = self._transformando_dados_tabela()
        with open (path,"w") as file:
            writer = csv.writer(file)
            writer.writerows(dados_combinados_tabela)
        print('Dados carregados com sucesso')
    