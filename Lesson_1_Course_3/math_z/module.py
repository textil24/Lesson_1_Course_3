import json
import os
import math
from math_z.unique_id import get_unique_id

# Указываем что можно импортировать 
__all__ = ['calculate', 'convert_precision', 'get_standard_deviation']

# Считает знаки после запятой 
def convert_precision():
    config_file = "assets/config.json"
    if os.path.exists(config_file):
        with open("assets/config.json", encoding='utf-8') as f:
            SETTINGS = json.load(f)
    else:
        print('Нет файла config.json')


    return len(str(round(1 / float(SETTINGS['precision'])))) - 1


# Вычислить среднеквадратичное отклоненине с заданной точностью
def get_standard_deviation(list):
    params_first = sum(list) / len(list)
    params_final = math.sqrt(
            sum((x - params_first) ** 2 for x in list) / len(list)
        )
    return round(params_final, convert_precision())

def calculate(op1, op2, act):

    """
    операции:
        '+' - сложение;
        '-' - вычитание;
        '*' - умножение;
        '/' - деление;
        '//' - целочисленное деление;
        '^' - возведение в степень;
        '%' - взятие остатка от деления;
    """

    with open('assets/actions.json', encoding='utf-8') as file:
        last_operations = json.load(file)

    if act == "+":
        r = op1 + op2
    elif act == "-":
        r = op1 - op2
    elif act == "*":
        r = op1 * op2
    elif act == "/":
        if op2 != 0:
            r = op1 / op2
        else:
            r = "деление на ноль невозможно"
    elif act == "^":
        r = op1**op2
    elif act == "//":
        r = op1 // op2
    elif act == "%":
        r = op1 % op2
    else:
        r = "операция не распознана"
    

    last_operations[get_unique_id()] = {
        'number_1': op1,
        'number_2': op2,
        'operation': act,
        'result': r,
        'full_action': f'{op1} {act} {op2} = {r}',
    }

    with open('assets/actions.json', 'w', encoding='utf-8') as file:
        json.dump(last_operations, file, indent=4, ensure_ascii=False)

    return r
