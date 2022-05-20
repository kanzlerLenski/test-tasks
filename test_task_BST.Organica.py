# task № 1

candidates = [
 {"name": "Vasya",  "scores": {"math": 58, "russian_language": 62,
                               "computer_science": 48}, "extra_scores":0},
 {"name": "Fedya",  "scores": {"math": 33, "russian_language": 85,
                               "computer_science": 42},  "extra_scores":2},
 {"name": "Petya",  "scores": {"math": 92, "russian_language": 33,
                               "computer_science": 34},  "extra_scores":1},
 {"name": "Olya",  "scores": {"math": 30, "russian_language": 100,
                               "computer_science": 30},  "extra_scores":1},
 {"name": "Oksana",  "scores": {"math": 65, "russian_language": 38,
                               "computer_science": 65},  "extra_scores":1},
  {"name": "Zhenya",  "scores": {"math": 90, "russian_language": 38,
                               "computer_science": 40},  "extra_scores":1}
]

def find_top_20(candidates):
    
    top = 20
    
    for person in candidates:
        person['total'] = person['scores']['math'] + \
                          person['scores']['russian_language'] + \
                          person['scores']['computer_science'] + \
                          person['extra_scores']

    sorted_list = sorted(candidates, key=lambda x: (x['total'],
                         x['scores']['computer_science'], x['scores']['math']),
                         reverse=True)

    result = [x['name'] for x in sorted_list[:top]]

    return result

# print(find_top_20(candidates))

# task № 2

names = ["Vasya", "Alice", "Petya", "Jenny", "Fedya", "Viola", "Mark", "Chris",
         "Margo"]
birthday_years = [1962, 1995, 2000, None, None, None, None, 1998, 2001]
genders = ["Male", "Female", "Male", "Female", "Male", None, None, None, None]

def get_inductees(names, birthday_years, genders):

    year = 2021
    inductees = []
    lost_data = []

    for i in range(len(names)):
        
        if genders[i] == 'Female':
            continue

        elif (birthday_years[i] == None) or (genders[i] == None):
            lost_data.append(names[i])
            
        elif genders[i] == 'Male' and 18 <= year - birthday_years[i] <= 30:
            inductees.append(names[i])

    print(f'Список призывников: {inductees}\n\n',
          'Список возможных призывников (однозначный ответ невозможен ',
          f'из-за потери данных): {lost_data}')

    return inductees, lost_data

# print(get_inductees(names, birthday_years, genders))

# task № 3

know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]

def find_athlets(know_english, sportsmen, more_than_20_years):

    candidates = [set(know_english), set(sportsmen), set(more_than_20_years)]
    
    return candidates.pop().intersection(*candidates)

# print(find_athlets(know_english, sportsmen, more_than_20_years))

# task № 4

students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923,
                       'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973,
                       'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936,
                       'Zoi': 4.937}

from openpyxl import Workbook
import os

def make_report_about_top3(students_avg_scores):

    top = 3

    sorted_scores = sorted(students_avg_scores.items(), key=lambda x: x[1],
                           reverse=True)

    book = Workbook()
    sheet = book.active

    sheet.append(('Имя студента_ки', 'Средний балл'))

    for score in sorted_scores[:top]:
        sheet.append(score)

    book.save('top_3_students.xlsx')

    return f"Файл находится здесь: {os.path.abspath('top_3_students.xlsx')}"

# print(make_report_about_top3(students_avg_scores))
