# Прочтите ранее созданный фаил с псевдоименами и произведением чисел и запишите его в JSON фаил 
# Напишите функцию, которая создает из созданного ранее файла фаил с новыми данными в формате JSON
# имена пишите с большой буквы
# Каждую пару сохраняйте с новой строки

import os
import json

def read_txt_and_save_to_JSON(file_name:str):
    if os.path.exists(file_name):
        work_dict = {}
        with open(file_name , 'r' , encoding='utf-8') as file:
            for line in file:
                work_dict[line[:-1].split('  ')[0].title()] = line[:-1].split('  ')[1]
        with open((file_name.split('.')[0] + '.json') , 'w' , encoding='utf-8') as file:
            json.dump(work_dict , file, ensure_ascii=False , indent=4)
            

read_txt_and_save_to_JSON('DATA/rezult.dat')