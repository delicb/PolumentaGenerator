"""
Оригинални полумента генератор се може наћи на
https://github.com/vl4dimir/polumenta/blob/master/index.php

Ово је само пајтон верзија исте ствари.
"""
import random
from datetime import datetime

start = [
	"Б", "В", "Г", "Д", "Ђ", "Ж", "З", "Ј", "К", "Л", "Љ", "М", "Н", "Њ", "П",
	"Р", "С", "Т", "Ћ", "Ф", "Х", "Ц", "Ч", "Џ", "Ш", "Б", "В", "Г", "Д", "Ђ",
	"Ж", "З", "Ј", "К", "Л", "Љ", "М", "Н", "Њ", "П", "Р", "С", "Т", "Ћ", "Ф",
	"Х", "Ц", "Ч", "Џ", "Ш", "Бл", "Бр", "Вл", "Вр", "Гл", "Гр", "Дл", "Др",
	"Жл", "Зл", "Зр", "Кр", "Кл", "Мр", "Мл", "Пј", "Пл", "Пљ", "Пњ", "Пр",
	"Св", "Сл", "См", "Сп",	"Ст", "Тл", "Тр", "Фл", "Фљ", "Фњ", "Фр", "Хл",
	"Хр",
]
middle = [
	"а", "е", "и", "о", "у", "р",
]
end = [
	"б", "в", "г", "д", "ђ", "ж", "з", "ј", "к", "л", "љ", "м", "н", "њ", "п",
	"р", "с", "т", "ћ", "ф", "х", "ц", "ч", "џ", "ш",
]
bad = set([	"л", "р", "ј", "љ", "њ", "Ђ", "Ж", "Ј", "Л", "Љ",
			"Н", "Њ", "Р", "Ћ", "Ч", "Џ", "Ш", ])

sufix = "о Полумента"

def generate():
    random.seed(datetime.now().timestamp())
    first = random.choice(start)
    second = random.choice(middle)
    while second == 'р':
        if first in bad:
            second = random.choice(middle)
        else:
            break
    third = random.choice(end)
    return first + second + third + sufix

if __name__ == '__main__':
    print(generate())
