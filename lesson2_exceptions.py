import random

def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except:
        print('Введите число больше нуля!')
parts=5
while parts!=1:
    parts = random.randint(1,100)
    cut_cake(parts)