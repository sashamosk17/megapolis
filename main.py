import csv

with open('students.csv', encoding='utf8') as ffile:
    reader = csv.reader(ffile, delimiter = ',')
    answer = list(reader)[1:]

    count_class = {}
    sum_class = {}
    for id, name, titleProject_id, level, score in answer:
        if('Хадаров Владимир' in name):
            print(f'Ты получил: {score}, за проект - {titleProject_id}')

        count_class[level] = count_class.get(level,0) + 1
        # if score != 'None':
        #     score = int(score)
        # else:
        #     score = 0
        sum_class[level] = sum_class.get(level,0) + int(score) if score != 'None' else 0

    for element in answer:
        if(element[-1] == 'None'):
            element[-1] = round(sum_class[element[-2]] / count_class[element[-2]],3)

with open('student_new.csv','w', encoding='utf8', newline='') as ffile:
    w = csv.writer(ffile)
    w.writerow(['id', 'Name', 'titleProject_id', 'class', 'score'])
    w.writerows(answer)


import csv

with open('students.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar = '"'))

    for i in range(len(reader)):
        j = i - 1
        key = reader[i]
        while (float(reader[j]['score'] if reader[j]['score'] != 'None' else 0 ) <
               float(key['score'] if key['score'] != 'None' else 0 ) and j >=0) :
            reader[j + 1] = reader[j]
            j-=1

        reader[j+1] = key

print('10 класс')
cnt = 1

for el in reader:
    if('10' in el['class']):
        surname,name, patre = el['Name'].split()
        print(f'{cnt} место: {name[0]}. {surname}')
        cnt+=1
    if cnt == 4:
        break


import csv

with open('students.csv', encoding='utf8') as f:
    reader = list(csv.DictReader(f, delimiter=',', quotechar='"'))
    data = sorted(reader, key=lambda x: x['titleProject_id'])
    # for i in range(len(reader)):
    #     j = i - 1
    #     key = reader[i]
    #     while( float(reader[j]['titleProject_id'] if reader[j]['titleProject_id'] != 'None' else 0) <
    #            float(key['titleProject_id'] if key['titleProject_id'] != 'None' else 0) and j >= 0):
    #         reader[j + 1] = reader[j]
    #         j -= 1
    #     reader[j + 1] = key

id_project = input()
while(id_project!= 'СТОП'):
    id_project = int(id_project)
    for el in data:
        if(int(el['titleProject_id']) == id_project):
            surname, name, patre = el['Name'].split(' ')
            print(f'Проект № {id_project} делал: {name[0]}. {surname} он(а) получил(а) оценку - {el["score"]}.')
            break
    else:
        print('Ничего не найдено')
    id_project = input()


import csv
import string
import random

def create_initials(s: string):
    names = s.split()
    return f'{names[0]}_{names[1][0]}_{names[2][0]}'

def create_password():
    letters = string.ascii_letters + string.digits
    password = ''.join(random.choice(letters) for _ in range(8))
    return password

stud_with_passwords = []
with open('students.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for row in reader:
        row['login'] = create_initials(row['Name'])
        row['password'] = create_password()
        stud_with_passwords.append(row)

with open('student_new.csv', 'w', encoding='utf8', newline='') as ffile:
    w = csv.DictWriter(ffile, fieldnames=['id','Name','titleProject_id','class','score', 'login', 'password'])
    w.writeheader()
    w.writerows(stud_with_passwords)

import csv
import string


def generate_hash(s: str):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    d = {l: i for i, l in enumerate(alphabet, 1)}
    p = 67
    m = 1e9 + 9
    hash_value = 0
    p_pow = 1
    for c in s:
        hash_value = (hash_value + d[c] * p_pow) % m
        p_pow = (p_pow * p) % m
    return int(hash_value)

students_with_hash = []
with open('students.csv', encoding='utf8') as file:
    reader = list(csv.DictReader(file, delimiter=',', quotechar='"'))
    for row in reader:
        row['id'] = generate_hash(row['Name'])
        students_with_hash.append(row)

with open('student_new.csv', 'w', encoding='utf8', newline='') as file:
    w = csv.DictWriter(file, fieldnames=['id','Name','titleProject_id','class','score'])
    w.writeheader()
    w.writerows(students_with_hash)