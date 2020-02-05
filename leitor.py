import csv

class CSV:
        
    def ler_csv(arquivo_csv):    
        with open(arquivo_csv,"r") as csvfile:
            spamreader = csv.reader(csvfile, delimiter = ",")
            line_count = 0
            for row in spamreader:
                if line_count == 0:
                    print(f'{"  ".join(row)}')
                    line_count += 1
                else:
                    for linha in row:
                        print(linha)
                    line_count += 1
                print(f"linhas processadas {line_count}")
                
    
    def escrever_csv(arquivo_csv, dados):
        with open(arquivo_csv, "w") as csvfile:
            csvwrite = csv.writer(csvfile, ",")
            csvwrite.writerow(dados)
        



