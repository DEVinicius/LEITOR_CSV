import csv

class WorkCSV:
        
    def read_csv(self, file_csv):    
        with open(file_csv,"r") as csvfile:
            spamreader = csv.reader(csvfile, delimiter = ",")
            line_count = 0
            for row in spamreader:
               # if line_count == 0:
                print(f'{"  |".join(row)}')
                print("")
                
    
    def write_csv(self, file_csv, data):
        field_name = list()
        
        for fdict in data:
            field_name.append(fdict)

        with open(file_csv, "w") as csvfile:
            csvwrite = csv.DictWriter(csvfile, fieldnames = field_name)
            csvwrite.writeheader()
            csvwrite.writerow(data)
        



