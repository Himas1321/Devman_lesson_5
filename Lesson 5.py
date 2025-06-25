import file_operations
from faker import Faker
import random
import os


RUNIC_ABC = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}


def main():
    os.makedirs('card', exist_ok=True)
    faker = Faker('ru_RU')
    for number in range(1, 11):
        random_strength = random.randint(3, 18)
        random_agility = random.randint(3, 18)
        random_endurance = random.randint(3, 18)
        random_intelligence = random.randint(3, 18)
        random_luck = random.randint(3, 18)
        skill = [
            'Стремительный прыжок', 'Электрический выстрел', 'Ледяной удар',
            'Стремительный удар', 'Кислотный взгляд', 'Тайный побег',
            'Ледяной выстрел', 'Огненный заряд'
        ]

        random_skill = random.sample(skill, 3)
        runic_skill = []
        skill_1 = random_skill[0]
        skill_2 = random_skill[1]
        skill_3 = random_skill[2]

        for russian_letters in RUNIC_ABC:
            runic_letters = RUNIC_ABC[russian_letters]
            skill_1 = skill_1.replace(russian_letters, runic_letters)
            skill_2 = skill_2.replace(russian_letters, runic_letters)
            skill_3 = skill_3.replace(russian_letters, runic_letters)
        runic_skill.append(skill_1)
        runic_skill.append(skill_2)
        runic_skill.append(skill_3)

        card = {
            "first_name": faker.first_name_male(),
            "last_name": faker.last_name_male(),
            "job": faker.job(),
            "town": faker.city(),
            "strength": random_strength,
            "agility": random_agility,
            "endurance": random_endurance,
            "intelligence": random_intelligence,
            "luck": random_luck,
            "skill_1": skill_1,
            "skill_2": skill_2,
            "skill_3": skill_3
        }

        form = "card/form_{}.svg".format(number)
        file_operations.render_template("charsheet.svg", form, card)


if __name__ == "__main__":
    main()
