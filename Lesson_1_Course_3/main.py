import math_z

if __name__ == "__main__":
    # тесты
    # from tests import run_all_tests
    # run_all_tests()

    print('Выбор функций: \n', '1) Калькулятор \n', '2) Узнать среднеквадратичное отклоненине с заданной точностью \n', '3) Настройки \n'  )
    number = int(input('Номер функции: '))
    if number == 1:
      number_1 = float(input("Операнд 1: "))
      number_2 = float(input("Операнд 2: "))
      operation = input("Оператор: ")
      print(f"Результат: {math_z.calculate(number_1, number_2, operation)}")
    elif number == 2:
      number_count = int(input('Введите количество чисел: '))

      number_list = []
      for item in range(number_count):
          current_number = int(input(f'Введите число {item+1}: '))
          number_list.append(current_number)

      print('Cреднеквадратичное отклоненине с заданной точностью: ', math_z.get_standard_deviation(number_list))

    elif number == 3:
      print('Текущие количество нулей в precision: ', math_z.convert_precision())
    else:
      print('Такого номера функции нет!')