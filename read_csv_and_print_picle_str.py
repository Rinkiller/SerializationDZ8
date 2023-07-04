# Прочтите созданный фаил без использования csv.DictReader
# Распечатайте его как Picle строку

import os
import pickle
import csv

def print_picleSTR_of_csvFile(csv_file_name:str):
    if os.path.exists(csv_file_name):
        with open(csv_file_name , 'r', newline='') as file:
            csv_Date = csv.reader(file)
            for line in csv_Date:
                print(pickle.dumps(line))

    

print_picleSTR_of_csvFile('DATA/file1.csv')
