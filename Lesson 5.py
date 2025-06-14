import file_operations
from faker import Faker
import random

name_file = Faker("ru_RU")
fake_first_name = Faker("ru_RU") 
fake_last_name = Faker("ru_RU")
fake_job = Faker("ru_RU")
fake_town = Faker("ru_RU")

random_strength = random.randint(3, 18)
random_agility = random.randint(3, 18)
random_endurance = random.randint(3, 18)
random_intelligence = random.randint(3, 18)
random_luck = random.randint(3, 18)

skill = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар", "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]
# skill_2 = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар", "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]
# skill_3 = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар", "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]
random_skill = random.sample(skill, 3)
# random_skill_2 = random.sample(skill_1, 1)
# random_skill_3 = random.sample(skill_1, 1)
runic_skill = []
runic_abc = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


skill_1 = random_skill[0]
skill_2 = random_skill[1]
skill_3 = random_skill[2]

for russian_letters in runic_abc:
    runic_letters = runic_abc[russian_letters]
    skill_1 = skill_1.replace(russian_letters, runic_letters)
    skill_2 = skill_2.replace(russian_letters, runic_letters)
    skill_3 = skill_3.replace(russian_letters, runic_letters)
runic_skill.append(skill_1)
runic_skill.append(skill_2)
runic_skill.append(skill_3)



name_surname = {
    "first_name": fake_first_name.first_name_male(), 
    "last_name": fake_last_name.last_name_male(),
    "job": fake_job.job(),
    "town": fake_town.city(),
    "strength": random_strength,
    "agility": random_agility,
    "endurance": random_endurance,
    "intelligence": random_intelligence,
    "luck": random_luck,
    "skill_1": skill_1,
    "skill_2": skill_2,
    "skill_3": skill_3
}





 # file_operations.render_template("charsheet.svg", "result.svg", name_surname)

for result in range(2):
     file_operations.render_template("charsheet.svg", "result.svg", name_surname)


#     f = open("result.svg")
#     f.format("result_1")

# file_1.format('1')



