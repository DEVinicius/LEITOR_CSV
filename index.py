from leitor import CSV

arquivo = 'Produtos.csv'
leitor = CSV()

leitor.read_csv(arquivo)

# dados = {
#     "Codigo" : "42424",
#     "Nome_produto" : "Notebook",
#     "Preco_compra": 10,
#     "Preco_Venda" : 20,
#     "Lucro": 100,
#     "Marca" : "Samsung",
#     "Quantidade" : 30 
# }

# nome_campos = list()

# for fdict in dados:
#     nome_campos.append(fdict)

# print(nome_campos)

#leitor.write_csv(arquivo,dados)