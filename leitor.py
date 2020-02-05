import csv

class CSV:
        
    def read_csv(file_csv):    
        with open(arquivo_csv,"r") as csvfile:
            spamreader = csv.reader(csvfile, delimiter = ",")
            line_count = 0
            for row in spamreader:
                if line_count == 0:
                    print(f'{"  ".join(row)}')
                    line_count += 1
                else:
                    for line in row:
                        print(line)
                    line_count += 1
                print(f"linhas processadas {line_count}")

    
    def write_csv(file_csv, data):
        with open(file_csv, "w") as csvfile:
            csvwrite = csv.writer(csvfile, ",")
            csvwrite.writerow(data)
        



