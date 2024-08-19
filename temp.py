# temp.py
'''
import os

from dotenv import load_dotenv

load_dotenv()
# Теперь переменная TOKEN, описанная в файле .env,
# доступна в пространстве переменных окружения.

token = os.getenv('TOKEN')
print(token)
'''


'''class NegativeValueException(Exception):  # Исключение, которое выбросим,
    pass                                  # если получено число меньше нуля.

def set_robot_power(value):
    if value < 0:
        raise NegativeValueException('Введите число, которое больше нуля!')

set_robot_power(-1)'''


def just_plus(first, second):
    # Ожидаются параметры одинакового типа.
    # В ином случае должна выбрасываться ошибка.
    try:
        print(first + second)
    except TypeError as e:
        print(e)


first = 'Why'
second = 10
just_plus(first, second)
