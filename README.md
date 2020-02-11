# LEITOR_CSV

Esta aplicação tem como objetivo criar uma classe genérica em python para leitura e inserção de dados em um banco criado em csv 
para que haja uma facilidade na manipulação dos dados. Há diversas outras bibliotecas para trabalhar de forma mais simples com
arquivos csv, não obstante, busquei criar minha própria classe, fazendo com que dicionários sejam inseridos e em qualquer arqui-
vo CSV, esteja ele vazio ou não, eu consiga manipular ele e realizar o trabalho da forma mais simples o possível.

# Inserção de DADOS

A classe criada só aceita dados vindo de dicionários, para que os parâmetros do banco em CSV sejam mantidos.

# Para utilizar a Classe

Para começar a utilizar a classe criada, primeiro deve importar o arquivo com a seguinte linha de código no seu arquivo:

from leitor import csv

Instancie a classe e utilize as funções que ela lhe permite utilizar.

# Função read_csv

Esta função apenas exige que o arquivo.csv seja colocado como parâmetro

# Função write_csv

Nesta função dois parâmetros devem ser passados.

1º - O Arquivo .csv

2º - O Dicionário com os dados a serem inseridos, com as chaves possuindo os mesmos nomes que as linhas do arquivo .csv
