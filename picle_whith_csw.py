# Напишите функцию которая преобразует picle файл в csv
# для тестирования возьмите picle версию файла из задачи 4 этого семинара
# функция должна извлекать ключи словаря для заголовков столбцов из переданного файла
import os
import pickle
import csv
def read_picle_file_and_write_csv_file(picle_file_name:str) -> None:
    if os.path.exists(picle_file_name):
        with(open(picle_file_name , 'rb') as file_picle_r,
            open((picle_file_name.split('.')[0] + '.csv'),'w' ) as file_csv_w):
            worc_dict = pickle.load(file_picle_r)
            if worc_dict.__class__ == list:
                csv_writer = csv.DictWriter(file_csv_w , fieldnames=[key for key in worc_dict[0]], restval='None',dialect='excel-tab',quoting=csv.QUOTE_ALL)
                csv_writer.writeheader()
                for item in worc_dict:
                    date = []
                    # for i , dict_row in enumerate(worc_dict.values()):
                    date.append(item)
                    csv_writer.writerows(date)
            elif worc_dict.__class__ == dict:
                csv_writer = csv.DictWriter(file_csv_w , fieldnames=[key for key in worc_dict], restval='None',dialect='excel-tab',quoting=csv.QUOTE_ALL)
                csv_writer.writeheader()
                date = []
                date.append(worc_dict)
                csv_writer.writerows(date)
    else:
        raise Exception(f'File {picle_file_name} not found!')    

read_picle_file_and_write_csv_file('DATA/file23.picle')