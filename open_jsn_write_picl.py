# Напишите функцию которая ищет в указанной директории json файлы 
# и сохраняет их сoдержимое в виде одноименных picle 
import json
import os
import pickle
# предварительно создал два json файла в папке DATA
# dict1 = {'name':'andrei','age':27,'weigth':78,'ocinki':{'math':4,'fizic':5,'biologi':4}}
# dict2 = [{'id':1,'data':[1,3,4,6,3,6,8,5]},{'id':2,'data':[8,5,6,6,36,6,8,5]},{'id':3,'data':[9,3,0,6,3,0,7,5]}]

# with (open('DATA/file1.json','w',encoding='utf-8') as f1, 
#       open('DATA/file23.json','w',encoding='utf-8') as f2):
#     json.dump(dict1 , f1)
#     json.dump(dict2 , f2)  
def open_jsn_write_picle(dir_name:str) -> None:
    os.chdir(dir_name)
    count = 0
    for file in os.listdir():
        if os.path.isfile(file):
            try:
                file_name , file_ext = file.split('.')
                if file_ext == 'json':
                    with (open(file , 'r',encoding='utf-8') as file_json_r , 
                          open((file_name + '.' + 'picle') , 'wb') as file_picle_w):
                        work_dict = json.load(file_json_r)
                        pickle.dump(work_dict , file_picle_w)
                        count += 1
            except Exception:
                pass
    print(f'Было обнаружено и перезаписано в формате picle {count} json-вских файлов')

open_jsn_write_picle('DATA')