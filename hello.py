import random

x = random.randint(0, 10)


def more_or_less(num):
    if x > 4:
        print('More')
    else:
        print('Less')    

more_or_less(x)