from config import DATA_ADDRESS
from class_Candidate import Candidate
import json


# загрузка из json в список
def load_candidates_from_json(address):
    with open(address, 'r', encoding='utf-8') as file:
        list_ = json.load(file)
        return list_


# создание обьектов класса candidate и запаковка их в список
def get_objects_list(list_):
    objects_list = []
    for i in list_:
        objects_list.append(
            Candidate(i["id"], i["name"], i["picture"], i["position"], i["gender"], i["age"], i["skills"]))
    return objects_list


# загрузка файла и получение списка в одном блоке
def load_data():
    data_from_json = load_candidates_from_json(DATA_ADDRESS)
    objects_list = get_objects_list(data_from_json)
    return objects_list


# возвращает кандидата по id
def get_candidate(cand_id):
    candidates_list = load_data()
    for object_ in candidates_list:
        if object_.id == cand_id:
            return object_
    return None


# список кандидатов по имени
def get_candidates_by_name(cand_name):
    candidates_list = load_data()
    cand_name_list = cand_name.strip().lower().split()
    output_set = set()
    for object_ in candidates_list:
        for cand in cand_name_list:
            if cand in object_.get_name_in_list():
                output_set.add(object_)
    return output_set


# список кандидатов по скиллам
def get_candidates_by_skill(cand_skill):
    candidates_list = load_data()
    output_list = []
    for object_ in candidates_list:
        if cand_skill.lower() in object_.get_skills_list():
            output_list.append(object_)
    return output_list
