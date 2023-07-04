# Урок 8. Сериализация
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
# Результаты обхода сохраните в файлы json, csv и pickle.
# 
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий.

import os
import json
import csv
import pickle


def reading_other_dir_and_save_to_json_csv_picle(dir_name_read:str) -> None:
    
    dir_dict = {}
    for dir_pth , dir_name , file_name in os.walk(dir_name_read):
        #print(f'{dir_pth=}\n{dir_name=}\n{file_name=}')
        if len(dir_name) == 0: dir_name = None
        if len(file_name) == 0: file_name = None 
        
        if file_name != None:
            list_of_file_name =[]
            for file in file_name:
                # with open((dir_pth +'\\'+ file), 'r') as f:
                #     #print(f'{f.__sizeof__=}')
                file_size = os.path.getsize(dir_pth + '\\' + file)
                list_of_file_name.append(file + ' SIZE = ' + str(file_size) + 'b')
        dir_dict[dir_pth.split('\\')[-1]] = {'Directori' : dir_name , 'Files' : list_of_file_name}
    with (open(dir_name_read.split('\\')[-1] + '.json', 'w',encoding='utf-8') as file_json , 
          open(dir_name_read.split('\\')[-1] + '.csv', 'w',encoding='utf-8') as file_csv ,
           open(dir_name_read.split('\\')[-1] + '.picle', 'wb') as file_picle ):
        json.dump(dir_dict , file_json , ensure_ascii=False,indent=3)
        csv_writer = csv.DictWriter(file_csv , fieldnames=[key for key in dir_dict], restval='None',dialect='excel',quoting=csv.QUOTE_ALL)
        csv_writer.writeheader()
        csv_writer.writerows([dir_dict])
        pickle.dump(dir_dict , file_picle)
reading_other_dir_and_save_to_json_csv_picle(os.getcwd())
