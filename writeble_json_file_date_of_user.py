# Напишите функцию, которая в бесконечном циклe запрашивает у пользователя имя, личный индентификатор 
# и уровень доступа ( от 1 до 7)
# После каждого ввода добавляет новую информацию в json фаил
# Пользователи группируются по уровню доступа
# Индентификатор пользователя выступает ключем для имени
# Убедитесь, что все индентификаторы уникальны независимо от уровня доступа
# При перезапуске функции все сохраненные ранее данные в файле должны сохраниться

import os
import json
import random

#   {1:{4657575:'ВАСЯ' , 356235:'Петя'} , 2 :{4645457:'ЮРА'}}

def owerwritebl_in_json_user_pass(file_name:str):
    while True:
        with open(file_name , 'r' , encoding='utf-8') as file:
            if len(file.readline()) == 0:
                worc_dict = {}
            else:
                file.seek(0,0)
                worc_dict = json.load(file)
            print(f'{worc_dict=}')
            try:
                level , user_name = input('Введите уровень доступа и имя пользователя через пробел: ').split(' ')        
                if level.isdigit() and 0 < int(level) < 8:
                    while True:
                        user_id = random.randint(10_000 , 100_000)
                        if user_id not in worc_dict:
                            if level not in worc_dict.keys():
                                worc_dict[level] = [{user_name : user_id}]
                            else:
                                worc_dict[level].append({user_name : user_id})
                            with open(file_name , 'w' , encoding='utf-8') as file:
                                json.dump(worc_dict , file , ensure_ascii=False , sort_keys=True)
                            break
                        else:
                            print('Inorrect input!!!')                    
            except :
                break
owerwritebl_in_json_user_pass('DATA/user_pass.json')
