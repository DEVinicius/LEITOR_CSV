from leitor import CSV

#Instancia da Classe e criacao da variavel arquivo
arquivo = 'Produtos.csv'
leitor = CSV()

#método para ler o arquivo
leitor.read_csv(arquivo)

# Dicionario que trabalha para inserir arquivos no banco .csv
dados = {
    "Codigo" : "42424",
    "Nome_produto" : "Notebook",
    "Preco_compra": 10,
    "Preco_Venda" : 20,
    "Lucro": 100,
    "Marca" : "Samsung",
    "Quantidade" : 30 
}

#Método para inserir dados no banco .csv
leitor.write_csv(arquivo,dados)