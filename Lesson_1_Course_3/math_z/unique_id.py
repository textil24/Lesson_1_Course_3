import datetime

def get_unique_id():

    # Создание уникального ключа
    now = datetime.datetime.now()
    current_data = f'{str(now.day).zfill(2)}.{str(now.month).zfill(2)}.{now.year}'
    current_time = f'{str(now.hour).zfill(2)}:{str(now.minute).zfill(2)}:{str(now.second).zfill(2)}'

    # Сам ключ
    unique_id = f'{current_time}|{current_data}'

    return unique_id
